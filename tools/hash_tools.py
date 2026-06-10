import hashlib
import bcrypt
from colorama import Fore

def hash_menu():
    print(f"""
{Fore.YELLOW}1. Hash de texto (MD5, SHA1, SHA256)
2. Hash de archivo
3. Verificar hash (crack simple)
4. Bcrypt (password hashing)
0. Volver""")
    op = input("Opción: ")
    
    if op == "1":
        text = input("Texto: ")
        print(f"MD5: {hashlib.md5(text.encode()).hexdigest()}")
        print(f"SHA1: {hashlib.sha1(text.encode()).hexdigest()}")
        print(f"SHA256: {hashlib.sha256(text.encode()).hexdigest()}")
    elif op == "2":
        file = input("Archivo: ")
        with open(file, "rb") as f:
            data = f.read()
            print(f"MD5: {hashlib.md5(data).hexdigest()}")
            print(f"SHA256: {hashlib.sha256(data).hexdigest()}")
    elif op == "3":
        target = input("Hash a crackear (MD5): ")
        wordlist = input("Wordlist (archivo): ")
        with open(wordlist, "r", encoding='latin-1') as f:
            for word in f:
                word = word.strip()
                if hashlib.md5(word.encode()).hexdigest() == target:
                    print(f"{Fore.GREEN}[+] Encontrado: {word}")
                    break
    elif op == "4":
        password = input("Password: ").encode()
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password, salt)
        print(f"Hash bcrypt: {hashed}")
        if bcrypt.checkpw(password, hashed):
            print("Verificación: OK")
    input("Enter...")
