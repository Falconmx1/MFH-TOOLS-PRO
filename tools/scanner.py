import socket

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def scan_menu():
    host = input("IP o dominio a escanear: ")
    ports = input("Puertos (separados por coma, ej: 22,80,443) o rango 1-1000: ")
    open_ports = []
    if '-' in ports:
        start, end = map(int, ports.split('-'))
        for port in range(start, end+1):
            if scan_port(host, port):
                open_ports.append(port)
                print(f"[+] Puerto {port} abierto")
    else:
        for port in map(int, ports.split(',')):
            if scan_port(host, port):
                open_ports.append(port)
                print(f"[+] Puerto {port} abierto")
    print(f"\nPuertos abiertos: {open_ports}")
    input("Enter para volver...")
