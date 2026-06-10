#!/usr/bin/env python3
import argparse
import sys
import os
import logging
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

# Configurar logging
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    filename=f"{LOG_DIR}/mfh_{datetime.now().strftime('%Y%m%d')}.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def show_banner():
    banner = f"""
{Fore.RED}{'='*50}
   __  ___  _   _   _____ _______        
  |  \/  | | | | | |_   _|__   __|       
  | \  / | | |_| |   | |    | |          
  | |\/| | |  _  |   | |    | |          
  |_|  |_| |_| |_|   |_|    |_|          
                                          
   {Fore.GREEN}MFH TOOLS PRO - Security Suite v2.0{Fore.RED}
   {Fore.CYAN}https://github.com/Falconmx1/MFH-TOOLS-PRO{Fore.RED}
{Fore.RED}{'='*50}{Style.RESET_ALL}
    """
    print(banner)

def main():
    parser = argparse.ArgumentParser(description="MFH TOOLS PRO - Suite de ciberseguridad")
    parser.add_argument("--tool", "-t", help="Ejecutar herramienta específica")
    parser.add_argument("--target", "-T", help="Target para la herramienta")
    parser.add_argument("--scan", "-s", help="Escaneo de puertos (ej: 192.168.1.1)")
    parser.add_argument("--ports", "-p", default="1-1000", help="Rango de puertos")
    parser.add_argument("--hash", help="Generar hash de un texto")
    parser.add_argument("--whois", help="Consulta whois de dominio")
    parser.add_argument("--geoip", help="GeoIP de IP")
    parser.add_argument("--report", "-r", help="Generar reporte en PDF/HTML")
    
    args = parser.parse_args()
    
    if len(sys.argv) == 1:
        show_banner()
        from tools.menu import interactive_menu
        interactive_menu()
        return
    
    # Modo CLI
    logging.info(f"Ejecución CLI con args: {vars(args)}")
    
    if args.scan:
        from tools.scanner import quick_scan
        quick_scan(args.scan, args.ports)
    elif args.hash:
        from tools.hash_tools import generate_hash
        generate_hash(args.hash)
    elif args.whois:
        from tools.whois_geo import get_whois
        get_whois(args.whois)
    elif args.geoip:
        from tools.whois_geo import get_geoip
        get_geoip(args.geoip)
    elif args.report:
        from tools.report import generate_report
        generate_report(args.report)
    else:
        print(f"{Fore.RED}[!] Herramienta no reconocida. Usa --help")

if __name__ == "__main__":
    main()
