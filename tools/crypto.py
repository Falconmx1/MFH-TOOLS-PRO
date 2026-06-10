from cryptography.fernet import Fernet

def crypto_menu():
    print("1. Generar clave 2. Cifrar archivo 3. Descifrar")
    op = input("Opción: ")
    if op == "1":
        key = Fernet.generate_key()
        with open("clave.key", "wb") as f:
            f.write(key)
        print("[+] Clave guardada en 'clave.key'")
    elif op == "2":
        file = input("Archivo a cifrar: ")
        with open("clave.key", "rb") as f:
            key = f.read()
        cipher = Fernet(key)
        with open(file, "rb") as f:
            encrypted = cipher.encrypt(f.read())
        with open(file + ".enc", "wb") as f:
            f.write(encrypted)
        print("[+] Archivo cifrado")
    input("Enter...")
