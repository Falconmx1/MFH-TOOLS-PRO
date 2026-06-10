import whois
import requests
from colorama import Fore

def whois_menu():
    domain = input("Dominio: ")
    print(whois.whois(domain))
    input("Enter...")

def get_whois(domain):
    print(whois.whois(domain))

def get_geoip(ip):
    r = requests.get(f"http://ip-api.com/json/{ip}").json()
    print(f"IP: {ip}\nPaís: {r['country']}\nCiudad: {r['city']}\nISP: {r['isp']}")
