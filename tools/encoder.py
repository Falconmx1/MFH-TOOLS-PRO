import base64
import codecs
from colorama import Fore

def encoder_menu():
    text = input("Texto a codificar/decodificar: ")
    print(f"""
{Fore.YELLOW}1. Base64 encode
2. Base64 decode
3. Hex encode
4. Hex decode
5. ROT13""")
    op = input("Opción: ")
    
    if op == "1":
        print(base64.b64encode(text.encode()).decode())
    elif op == "2":
        print(base64.b64decode(text).decode())
    elif op == "3":
        print(text.encode().hex())
    elif op == "4":
        print(bytes.fromhex(text).decode())
    elif op == "5":
        print(codecs.encode(text, 'rot_13'))
    input("Enter...")
