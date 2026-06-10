from PIL import Image
from colorama import Fore

def stego_menu():
    print(f"""
{Fore.YELLOW}1. Ocultar mensaje en imagen (LSB)
2. Extraer mensaje de imagen
3. Analizar posibles estegos""")
    op = input("Opción: ")
    
    if op == "1":
        img_path = input("Imagen original: ")
        msg = input("Mensaje a ocultar: ")
        img = Image.open(img_path)
        pixels = img.load()
        msg_bin = ''.join(format(ord(c), '08b') for c in msg) + '11111111'
        idx = 0
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if idx < len(msg_bin):
                    r, g, b = pixels[i, j]
                    r = (r & 0xFE) | int(msg_bin[idx])
                    pixels[i, j] = (r, g, b)
                    idx += 1
        img.save("stego_" + img_path)
        print(f"{Fore.GREEN}[+] Mensaje oculto en stego_{img_path}")
    elif op == "2":
        img_path = input("Imagen con estego: ")
        img = Image.open(img_path)
        pixels = img.load()
        bits = []
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = pixels[i, j]
                bits.append(str(r & 1))
                if len(bits) == 8:
                    char = chr(int(''.join(bits), 2))
                    if char == '\xff': break
                    print(char, end='')
                    bits = []
        print()
    input("Enter...")
