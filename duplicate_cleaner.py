#!/usr/bin/env python3
import os
import hashlib
import json
import shutil
import argparse
from datetime import datetime

MEMORY_FILE = "/home/majaolagunju/duplicate_memory.json"
TRASH_DIR = "/home/majaolagunju/.trash"

def compute_hash(file_path):
    """Compute SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def load_memory():
    """Load memory from JSON file, or initialize if it doesn't exist."""
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"scans": [], "last_updated": None}

def save_memory(memory):
    """Save memory to JSON file."""
    memory["last_updated"] = datetime.now().isoformat()
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def scan_duplicates(directory):
    """Scan directory for duplicate files and return grouped results."""
    hash_dict = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            path = os.path.join(root, filename)
            if os.path.isfile(path):
                file_hash = compute_hash(path)
                size = os.path.getsize(path)
                if file_hash not in hash_dict:
                    hash_dict[file_hash] = []
                hash_dict[file_hash].append({"path": path, "size": size, "status": "kept"})

    # Filter out non-duplicates
    duplicates = {h: files for h, files in hash_dict.items() if len(files) > 1}
    return duplicates

def log_scan(memory, directory, duplicates):
    """Log a scan session to memory."""
    scan = {
        "timestamp": datetime.now().isoformat(),
        "directory": directory,
        "duplicates": [
            {"hash": h, "files": files} for h, files in duplicates.items()
        ]
    }
    memory["scans"].append(scan)
    save_memory(memory)

def clean_duplicates(directory, dry_run=True):
    """Find and optionally clean duplicates, moving extras to trash."""
    duplicates = scan_duplicates(directory)
    if not duplicates:
        print("No duplicates found.")
        return

    memory = load_memory()
    total_freed = 0

    print("Duplicate Files Found:")
    for file_hash, files in duplicates.items():
        print(f"\nHash: {file_hash}")
        for i, file in enumerate(files):
            print(f"  {i+1}. {file['path']} ({file['size']} bytes)")

        if not dry_run and len(files) > 1:
            # Keep the first file, move others to trash
            for file in files[1:]:
                trash_path = os.path.join(TRASH_DIR, f"{os.path.basename(file['path'])}_{datetime.now().isoformat()}")
                if not os.path.exists(TRASH_DIR):
                    os.makedirs(TRASH_DIR)
                shutil.move(file["path"], trash_path)
                file["status"] = "moved"
                file["trash_path"] = trash_path
                total_freed += file["size"]
                print(f"  Moved to trash: {file['path']} -> {trash_path}")

    log_scan(memory, directory, duplicates)
    if not dry_run:
        print(f"\nSpace freed: {total_freed} bytes")

def query_memory():
    """Display history of scans and actions."""
    memory = load_memory()
    if not memory["scans"]:
        print("No scans recorded.")
        return

    for scan in memory["scans"]:
        print(f"\nScan at {scan['timestamp']} in {scan['directory']}:")
        for dup in scan["duplicates"]:
            print(f"  Hash: {dup['hash']}")
            for file in dup["files"]:
                status = file["status"]
                if status == "moved":
                    print(f"    {file['path']} -> {file['trash_path']} ({file['size']} bytes, {status})")
                else:
                    print(f"    {file['path']} ({file['size']} bytes, {status})")

def undo_last_scan():
    """Undo the last scan by restoring moved files from trash."""
    memory = load_memory()
    if not memory["scans"]:
        print("No scans to undo.")
        return

    last_scan = memory["scans"][-1]
    restored = 0

    for dup in last_scan["duplicates"]:
        for file in dup["files"]:
            if file["status"] == "moved" and "trash_path" in file:
                trash_path = file["trash_path"]
                original_path = file["path"]
                if os.path.exists(trash_path):
                    shutil.move(trash_path, original_path)
                    file["status"] = "restored"
                    restored += 1
                    print(f"Restored: {trash_path} -> {original_path}")

    save_memory(memory)
    if restored > 0:
        print(f"Restored {restored} files from last scan.")
    else:
        print("No files to restore from last scan.")

def main():
    parser = argparse.ArgumentParser(description="Duplicate file finder and cleaner with memory")
    parser.add_argument("directory", help="Directory to scan for duplicates")
    parser.add_argument("--clean", action="store_true", help="Clean duplicates (move to trash)")
    parser.add_argument("--dry-run", action="store_true", help="Simulate cleaning without moving files")
    parser.add_argument("--query", action="store_true", help="Query scan history")
    parser.add_argument("--undo", action="store_true", help="Undo last scan (restore files)")
    args = parser.parse_args()

    if args.query:
        query_memory()
    elif args.undo:
        undo_last_scan()
    else:
        dry_run = args.dry_run or not args.clean
        clean_duplicates(args.directory, dry_run=dry_run)

if __name__ == "__main__":
    main()
