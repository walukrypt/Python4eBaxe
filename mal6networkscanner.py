import socket

def scan_ports(target_ip, port_range):
    for port in range(1, port_range + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

target = "127.0.0.1"  # Localhost
scan_ports(target, 100)
