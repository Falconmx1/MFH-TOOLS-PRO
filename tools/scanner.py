import socket
from colorama import Fore

def scanner_menu():
    target = input("IP o dominio: ")
    ports = input("Puertos (ej: 22,80,443 o 1-1000): ")
    open_ports = []
    
    if '-' in ports:
        start, end = map(int, ports.split('-'))
        for port in range(start, end+1):
            if scan_port(target, port):
                open_ports.append(port)
                print(f"{Fore.GREEN}[+] Puerto {port} abierto")
    else:
        for port in map(int, ports.split(',')):
            if scan_port(target, port):
                open_ports.append(port)
                print(f"{Fore.GREEN}[+] Puerto {port} abierto")
    
    print(f"\n{Fore.CYAN}Puertos abiertos: {open_ports}")
    input("Enter...")

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def quick_scan(host, ports):
    for port in map(int, ports.split(',')):
        if scan_port(host, port):
            print(f"Puerto {port}: ABIERTO")
