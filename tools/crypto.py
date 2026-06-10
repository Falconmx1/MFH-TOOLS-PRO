from cryptography.fernet import Fernet
from Crypto.Cipher import AES
import os
from colorama import Fore

def crypto_menu():
    print(f"""
{Fore.YELLOW}1. Generar clave AES
2. Cifrar archivo (AES)
3. Descifrar archivo (AES)
4. Cifrar texto (Fernet)
0. Volver""")
    op = input("Opción: ")
    
    if op == "1":
        key = Fernet.generate_key()
        with open("clave.key", "wb") as f:
            f.write(key)
        print(f"{Fore.GREEN}[+] Clave guardada")
    elif op == "2":
        file = input("Archivo: ")
        with open("clave.key", "rb") as f:
            key = f.read()
        cipher = Fernet(key)
        with open(file, "rb") as f:
            encrypted = cipher.encrypt(f.read())
        with open(file + ".enc", "wb") as f:
            f.write(encrypted)
        print(f"{Fore.GREEN}[+] Cifrado: {file}.enc")
    elif op == "3":
        file = input("Archivo .enc: ")
        with open("clave.key", "rb") as f:
            key = f.read()
        cipher = Fernet(key)
        with open(file, "rb") as f:
            decrypted = cipher.decrypt(f.read())
        with open(file.replace(".enc", ""), "wb") as f:
            f.write(decrypted)
        print(f"{Fore.GREEN}[+] Descifrado")
    elif op == "4":
        text = input("Texto: ")
        key = Fernet.generate_key()
        cipher = Fernet(key)
        encrypted = cipher.encrypt(text.encode())
        print(f"{Fore.CYAN}Clave: {key.decode()}\nCifrado: {encrypted.decode()}")
    input("Enter...")
