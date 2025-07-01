import shutil
import os
from datetime import datetime

def backup_files(source_dir, backup_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
    shutil.copytree(source_dir, backup_path)

# Example: backup_files("/path/to/source", "/path/to/backup")
