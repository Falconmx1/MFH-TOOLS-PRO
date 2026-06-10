import requests
import socket
import dns.resolver
from colorama import Fore

def osint_menu():
    while True:
        print(f"""
{Fore.CYAN}╔══════════════════════════════╗
║      OSINT TOOLS MENU        ║
╠══════════════════════════════╣
║ 1. Whois de dominio          ║
║ 2. DNS lookup                ║
║ 3. GeoIP de IP               ║
║ 4. Subdomain finder          ║
║ 5. Email OSINT (Hunter)      ║
║ 0. Volver                    ║
╚══════════════════════════════╝{Fore.RESET}""")
        op = input("Opción: ")
        if op == "0": break
        elif op == "1":
            domain = input("Dominio: ")
            import whois
            print(whois.whois(domain))
        elif op == "2":
            domain = input("Dominio: ")
            for q in ['A', 'MX', 'NS', 'TXT']:
                try:
                    answers = dns.resolver.resolve(domain, q)
                    print(f"{q}: {[str(a) for a in answers]}")
                except: pass
        elif op == "3":
            ip = input("IP: ")
            response = requests.get(f"http://ip-api.com/json/{ip}").json()
            print(f"País: {response.get('country')}, Ciudad: {response.get('city')}")
        elif op == "4":
            domain = input("Dominio: ")
            subdomains = ['www', 'mail', 'ftp', 'admin', 'blog']
            for sub in subdomains:
                try:
                    socket.gethostbyname(f"{sub}.{domain}")
                    print(f"[+] {sub}.{domain}")
                except: pass
        elif op == "5":
            email = input("Email (ej: nombre@dominio.com): ")
            print("[!] Necesitas API key de Hunter.io para funcionar real")
        input("Enter para continuar...")
