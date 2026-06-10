from PIL import Image
import exifread
import PyPDF2
import os
from colorama import Fore

def metadata_menu():
    file = input("Archivo a analizar (jpg, png, pdf): ")
    
    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
        img = Image.open(file)
        print(f"Formato: {img.format}, Tamaño: {img.size}, Modo: {img.mode}")
        with open(file, 'rb') as f:
            tags = exifread.process_file(f)
            for tag in tags:
                print(f"{tag}: {tags[tag]}")
    elif file.lower().endswith('.pdf'):
        with open(file, 'rb') as f:
            pdf = PyPDF2.PdfReader(f)
            info = pdf.metadata
            for k, v in info.items():
                print(f"{k}: {v}")
    else:
        print("Formato no soportado. Usa JPG/PNG/PDF")
    input("Enter...")
