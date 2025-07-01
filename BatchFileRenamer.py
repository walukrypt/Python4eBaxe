import os

def rename_files(directory, prefix="file", start_num=1):
    for filename in os.listdir(directory):
        if filename.startswith(prefix):
            continue
        extension = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{start_num:03d}{extension}"
        os.rename(
            os.path.join(directory, filename),
            os.path.join(directory, new_name)
        )
        start_num += 1

# Example: rename_files("/path/to/folder", "photo", 1)
