import hashlib

def hash_menu():
    text = input("Texto a hashear: ")
    print(f"MD5: {hashlib.md5(text.encode()).hexdigest()}")
    print(f"SHA1: {hashlib.sha1(text.encode()).hexdigest()}")
    print(f"SHA256: {hashlib.sha256(text.encode()).hexdigest()}")
    input("Enter...")
