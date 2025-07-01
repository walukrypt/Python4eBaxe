import sys
import time

sys.argv[0] = "notepad.exe"  # Fake process name
while True:
    print("Running as 'notepad.exe'...")  # Replace with malicious action
    time.sleep(5)
