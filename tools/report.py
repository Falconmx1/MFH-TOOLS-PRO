from fpdf import FPDF
from datetime import datetime
from colorama import Fore

def report_menu():
    data = input("Texto del reporte (o archivo .txt): ")
    try:
        with open(data, 'r') as f:
            content = f.read()
    except:
        content = data
    
    print(f"{Fore.YELLOW}1. Reporte PDF\n2. Reporte HTML")
    op = input("Opción: ")
    
    if op == "1":
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="MFH TOOLS PRO - Reporte de Seguridad", ln=1, align='C')
        pdf.cell(200, 10, txt=f"Fecha: {datetime.now()}", ln=1, align='C')
        pdf.multi_cell(0, 10, txt=content)
        pdf.output("MFH_report.pdf")
        print(f"{Fore.GREEN}[+] Reporte PDF guardado")
    elif op == "2":
        with open("MFH_report.html", "w") as f:
            f.write(f"<html><body><h1>MFH TOOLS PRO</h1><h2>{datetime.now()}</h2><pre>{content}</pre></body></html>")
        print(f"{Fore.GREEN}[+] Reporte HTML guardado")
    input("Enter...")

def generate_report(format):
    report_menu()
