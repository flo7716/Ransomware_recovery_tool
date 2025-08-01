from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

def decrypt(file_path):
    key = input("Enter AES key (hex or utf-8): ").strip()
    iv = input("Enter IV (hex or utf-8): ").strip()

    try:
        # Convert key and IV to bytes
        if all(c in "0123456789abcdefABCDEF" for c in key) and len(key) % 2 == 0:
            key_bytes = bytes.fromhex(key)
        else:
            key_bytes = key.encode()

        if all(c in "0123456789abcdefABCDEF" for c in iv) and len(iv) % 2 == 0:
            iv_bytes = bytes.fromhex(iv)
        else:
            iv_bytes = iv.encode()

        with open(file_path, "rb") as f:
            ciphertext = f.read()

        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

        out_path = file_path.replace(".enc", "") + ".aes_decrypted.txt"
        with open(out_path, "wb") as f:
            f.write(plaintext)

        print(f"[+] AES decryption complete: {out_path}")

    except Exception as e:
        print("[-] AES decryption failed:", e)
