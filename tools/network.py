import subprocess
import platform
from colorama import Fore

def network_menu():
    target = input("IP o dominio: ")
    print(f"""
{Fore.YELLOW}1. Ping
2. Traceroute
3. Ver puertos abiertos""")
    op = input("Opción: ")
    
    if op == "1":
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        subprocess.call(['ping', param, '4', target])
    elif op == "2":
        cmd = 'tracert' if platform.system().lower() == 'windows' else 'traceroute'
        subprocess.call([cmd, target])
    elif op == "3":
        import socket
        for port in [21,22,80,443,3306]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((target, port)) == 0:
                print(f"Puerto {port}: ABIERTO")
            sock.close()
    input("Enter...")
