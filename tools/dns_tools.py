import dns.resolver
from colorama import Fore

def dns_menu():
    domain = input("Dominio: ")
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA']
    
    for q in record_types:
        try:
            answers = dns.resolver.resolve(domain, q)
            print(f"{q}: {[str(a) for a in answers]}")
        except:
            pass
    input("Enter...")
