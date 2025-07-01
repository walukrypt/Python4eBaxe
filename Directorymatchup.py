#!/usr/bin/env python3
import os
import shutil

def Directorymatchup(directory):
    print(f"Checking directory: {directory}")
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        print(f"Found: {filename}, Is file? {os.path.isfile(full_path)}")
        if os.path.isfile(full_path):
            extension = filename.split(".")[-1].lower()
            if extension:
                target_dir = os.path.join(directory, extension.upper())
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                print(f"Moving {filename} to {target_dir}")
                shutil.move(full_path, os.path.join(directory, target_dir, filename))
            else:
                print(f"Skipping {filename} - no extension")
        else:
            print(f"Skipping {filename} - not a file")


Directorymatchup("/home/majaolagunju/python4e")
