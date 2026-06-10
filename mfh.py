#!/usr/bin/env python3
import os
import sys
from tools.osint import osint_menu
from tools.scanner import scan_menu
from tools.crypto import crypto_menu
from tools.hash_tools import hash_menu

def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("=========================================")
    print("   __  ___  _   _   _____ _______        ")
    print("  |  \/  | | | | | |_   _|__   __|       ")
    print("  | \  / | | |_| |   | |    | |          ")
    print("  | |\/| | |  _  |   | |    | |          ")
    print("  |_|  |_| |_| |_|   |_|    |_|          ")
    print("                                          ")
    print("   MFH TOOLS PRO - Security Suite v1.0   ")
    print("   https://github.com/Falconmx1/MFH-TOOLS-PRO")
    print("=========================================")

def main_menu():
    while True:
        show_banner()
        print("\n[+] SELECCIONA UNA OPCIÓN:")
        print("1. OSINT (info dominios, emails)")
        print("2. Escáner de Puertos")
        print("3. Cifrado AES/GPG")
        print("4. Herramientas Hash (MD5, SHA)")
        print("5. Salir")
        
        op = input("\n Opción: ")
        if op == "1": osint_menu()
        elif op == "2": scan_menu()
        elif op == "3": crypto_menu()
        elif op == "4": hash_menu()
        elif op == "5": sys.exit(0)
        else: input("Opción no válida. Enter para continuar...")

if __name__ == "__main__":
    main_menu()
