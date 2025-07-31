import os
import base64
from core.utils import calculate_entropy

def analyze_file(filepath):
    entropy = calculate_entropy(filepath)
    filesize = os.path.getsize(filepath)

    print(f"[*] Entropy: {entropy:.4f}")
    print(f"[*] File size: {filesize} bytes")

    if filesize % 256 == 0 and entropy > 6.5:
        print("[+] Detected likely RSA-encrypted file.")
        return "RSA"
    
    if filesize % 16 == 0 and entropy > 5.5:
        print("[+] Detected likely AES-encrypted file.")
        return "AES"

    try:
        with open(filepath, 'rb') as f:
            data = f.read()

        # Try base64 decode to confirm
        base64.b64decode(data, validate=True)
        print("[+] Detected likely Base64-encoded file.")
        return "BASE64"

    except Exception:
        pass

    # Fallback: check for plaintext/XOR
    with open(filepath, 'rb') as f:
        data = f.read()
        if any(32 <= b <= 126 for b in data):
            print("[+] Detected weak or XOR-like encryption.")
            return "XOR"

    return "UNKNOWN"
