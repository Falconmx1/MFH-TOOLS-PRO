import requests
from colorama import Fore

def vuln_menu():
    url = input("URL (ej: http://ejemplo.com): ")
    print(f"{Fore.YELLOW}[*] Escaneando {url}")
    
    # SQLi test
    payloads = ["'", "1' OR '1'='1", "<script>alert(1)</script>"]
    for payload in payloads:
        r = requests.get(f"{url}?id={payload}")
        if "mysql" in r.text.lower() or "sql" in r.text.lower():
            print(f"{Fore.RED}[!] Posible SQL injection con: {payload}")
    
    # XSS test
    for payload in payloads:
        if payload in r.text:
            print(f"{Fore.RED}[!] Posible XSS con: {payload}")
    
    print(f"{Fore.GREEN}[+] Escaneo completado")
    input("Enter...")
