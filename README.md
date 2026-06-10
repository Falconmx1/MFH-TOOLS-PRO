# MFH TOOLS PRO - Cybersecurity Suite v2.0

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)

## 🛠️ 20+ Herramientas Incluidas

| Categoría | Herramientas |
|-----------|--------------|
| **OSINT** | Whois, DNS lookup, GeoIP, Subdomain finder, Email OSINT |
| **Escáner** | Puertos TCP/UDP, Vulnerabilidades (SQLi/XSS), Servicios |
| **Criptografía** | AES-256, Fernet, GPG (simulado), Bcrypt |
| **Hashes** | MD5, SHA1, SHA256, Crackeo básico |
| **Forensics** | Metadatos, Strings ocultos, Hash de archivos |
| **Red** | Ping, Traceroute, Escáner de puertos |
| **Web** | SQLi tester, XSS finder, Brute force HTTP |
| **Esteganografía** | LSB embed/extract, Análisis de imágenes |
| **Utilidades** | Password generator, Encoders (Base64/Hex/ROT13) |

## 🚀 Instalación Rápida

```bash
git clone https://github.com/Falconmx1/MFH-TOOLS-PRO.git
cd MFH-TOOLS-PRO
pip install -r requirements.txt
python3 mfh.py

🎯 Modo CLI (para scripts)
python3 mfh.py --scan 192.168.1.1 -p 22,80,443
python3 mfh.py --hash "Hola Mundo"
python3 mfh.py --whois google.com
python3 mfh.py --geoip 8.8.8.8
python3 mfh.py --report html
