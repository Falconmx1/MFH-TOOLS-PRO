import sys
from colorama import Fore, Style

def interactive_menu():
    from tools.osint import osint_menu
    from tools.scanner import scanner_menu
    from tools.crypto import crypto_menu
    from tools.hash_tools import hash_menu
    from tools.metadata import metadata_menu
    from tools.bruteforce import bruteforce_menu
    from tools.whois_geo import whois_menu
    from tools.network import network_menu
    from tools.encoder import encoder_menu
    from tools.exploit import exploit_menu
    from tools.forensic import forensic_menu
    from tools.steganography import stego_menu
    from tools.password_gen import password_menu
    from tools.vuln_scanner import vuln_menu
    from tools.dns_tools import dns_menu
    from tools.report import report_menu
    
    while True:
        print(f"""
{Fore.CYAN}╔════════════════════════════════════════╗
║        MFH TOOLS PRO - MENÚ PRINCIPAL     ║
╠════════════════════════════════════════╣
║ {Fore.YELLOW}1.{Fore.WHITE} OSINT (5 herramientas)              ║
║ {Fore.YELLOW}2.{Fore.WHITE} Escáner de Puertos                  ║
║ {Fore.YELLOW}3.{Fore.WHITE} Cifrado AES/GPG                     ║
║ {Fore.YELLOW}4.{Fore.WHITE} Herramientas Hash                   ║
║ {Fore.YELLOW}5.{Fore.WHITE} Análisis de Metadatos               ║
║ {Fore.YELLOW}6.{Fore.WHITE} Force Brute Básico                  ║
║ {Fore.YELLOW}7.{Fore.WHITE} Whois y GeoIP                       ║
║ {Fore.YELLOW}8.{Fore.WHITE} Herramientas de Red                 ║
║ {Fore.YELLOW}9.{Fore.WHITE} Codificadores (Base64, Hex)         ║
║ {Fore.YELLOW}10.{Fore.WHITE} Exploit Simple (Buffer Overflow)   ║
║ {Fore.YELLOW}11.{Fore.WHITE} Forense Digital                    ║
║ {Fore.YELLOW}12.{Fore.WHITE} Esteganografía (LSB)               ║
║ {Fore.YELLOW}13.{Fore.WHITE} Generador de Passwords             ║
║ {Fore.YELLOW}14.{Fore.WHITE} Escáner de Vulnerabilidades        ║
║ {Fore.YELLOW}15.{Fore.WHITE} Herramientas DNS                   ║
║ {Fore.YELLOW}16.{Fore.WHITE} Generar Reporte                    ║
║ {Fore.YELLOW}0.{Fore.RED} Salir                                 ║
╚════════════════════════════════════════╝{Style.RESET_ALL}""")
        
        op = input(f"\n{Fore.GREEN}[MFH]{Fore.WHITE} Opción: ")
        
        if op == "0": sys.exit(0)
        elif op == "1": osint_menu()
        elif op == "2": scanner_menu()
        elif op == "3": crypto_menu()
        elif op == "4": hash_menu()
        elif op == "5": metadata_menu()
        elif op == "6": bruteforce_menu()
        elif op == "7": whois_menu()
        elif op == "8": network_menu()
        elif op == "9": encoder_menu()
        elif op == "10": exploit_menu()
        elif op == "11": forensic_menu()
        elif op == "12": stego_menu()
        elif op == "13": password_menu()
        elif op == "14": vuln_menu()
        elif op == "15": dns_menu()
        elif op == "16": report_menu()
        else: input(f"{Fore.RED}[!] Opción inválida. Enter para continuar...")
