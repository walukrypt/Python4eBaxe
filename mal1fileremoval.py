import os

def file_deleter(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Simulating deletion of: {file_path}")
            # os.remove(file_path)  # Uncomment to actually delete (use with caution!)

target_dir = "test_folder"
file_deleter(target_dir)
import os

def file_deleter(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Simulating deletion of: {file_path}")
            # os.remove(file_path)  # Uncomment to actually delete (use with caution!)

target_dir = "test_folder"
file_deleter(target_dir)
