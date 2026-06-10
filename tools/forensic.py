import hashlib
import os
from colorama import Fore

def forensic_menu():
    file = input("Archivo a analizar: ")
    print(f"{Fore.CYAN}1. Calcular hash MD5/SHA256")
    print("2. Ver strings ocultos")
    print("3. Buscar archivos por extensión")
    op = input("Opción: ")
    
    if op == "1":
        with open(file, 'rb') as f:
            data = f.read()
            print(f"MD5: {hashlib.md5(data).hexdigest()}")
            print(f"SHA256: {hashlib.sha256(data).hexdigest()}")
    elif op == "2":
        with open(file, 'rb') as f:
            content = f.read().decode('latin-1')
            words = [w for w in content.split() if len(w) > 3]
            print("Posibles strings:", words[:20])
    elif op == "3":
        ext = input("Extensión (ej: .exe): ")
        for root, dirs, files in os.walk('/'):
            for file in files:
                if file.endswith(ext):
                    print(os.path.join(root, file))
    input("Enter...")
