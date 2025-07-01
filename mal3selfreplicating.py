import shutil
import os

def replicate():
    current_script = __file__
    for i in range(5):  # Limit to 5 copies
        new_name = f"copy_{i}_{os.path.basename(current_script)}"
        shutil.copy(current_script, new_name)
        print(f"Replicated to: {new_name}")

replicate()
