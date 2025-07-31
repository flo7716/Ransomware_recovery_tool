import math
import os
from core.utils import calculate_entropy

def analyze_file(filepath):
    entropy = calculate_entropy(filepath)
    filesize = os.path.getsize(filepath)

    if entropy > 7.8:
        if filesize % 16 == 0:
            print("[+] Detected likely AES-encrypted file.")
            return "AES"
        elif filesize % 256 == 0:
            print("[+] Detected likely RSA-encrypted file.")
            return "RSA"
        else:
            print("[?] High entropy but unknown block structure.")
    else:
        with open(filepath, 'rb') as f:
            data = f.read()
            if b'=' in data or b'==' in data[-10:]:
                print("[+] Detected likely Base64-encoded file.")
                return "BASE64"
            elif any(32 <= b <= 126 for b in data):  # ASCII printables
                print("[+] Detected weak or XOR-like encryption.")
                return "XOR"

    return "UNKNOWN"