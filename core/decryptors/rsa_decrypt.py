from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os

def decrypt(file_path):
    priv_path = input("Enter path to RSA private key (.pem): ").strip()
    try:
        with open(priv_path, "rb") as f:
            private_key = serialization.load_pem_private_key(f.read(), password=None)

        with open(file_path, "rb") as f:
            ciphertext = f.read()

        chunk_size = 256
        decrypted_chunks = []

        for i in range(0, len(ciphertext), chunk_size):
            chunk = ciphertext[i:i+chunk_size]
            decrypted_chunk = private_key.decrypt(
                chunk,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            decrypted_chunks.append(decrypted_chunk)

        out_path = file_path.replace(".enc", "") + ".rsa_decrypted.txt"
        with open(out_path, "wb") as f:
            for chunk in decrypted_chunks:
                f.write(chunk)

        print(f"[+] RSA decryption complete: {out_path}")

    except Exception as e:
        print("[-] RSA decryption failed:", e)
