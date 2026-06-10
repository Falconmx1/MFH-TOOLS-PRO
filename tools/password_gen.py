import random
import string
from colorama import Fore

def password_menu():
    length = int(input("Longitud: "))
    use_upper = input("Mayúsculas? (s/n): ").lower() == 's'
    use_digits = input("Dígitos? (s/n): ").lower() == 's'
    use_symbols = input("Símbolos? (s/n): ").lower() == 's'
    
    chars = string.ascii_lowercase
    if use_upper: chars += string.ascii_uppercase
    if use_digits: chars += string.digits
    if use_symbols: chars += string.punctuation
    
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"{Fore.GREEN}[+] Password: {password}")
    input("Enter...")
