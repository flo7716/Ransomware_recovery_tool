from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from cryptography.hazmat.primitives.asymmetric import rsa, padding as rsa_pad
from cryptography.hazmat.primitives import serialization, hashes
import base64
import os

# Create sample directory if needed
if not os.path.exists("samples"):
    os.makedirs("samples")

plaintext = b"This is a test message for ransomware recovery."

def gen_aes_sample():
    key = b"1234567890ABCDEF1234567890ABCDEF"  # 32-byte AES key
    iv = b"ABCDEF1234567890"                  # 16-byte IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(plaintext, AES.block_size))
    with open("samples/aes_sample.enc", "wb") as f:
        f.write(ct)
    print("[+] AES sample created with key and IV:")
    print(f"    Key (utf-8): {key.decode()}")
    print(f"    IV  (utf-8): {iv.decode()}")



def gen_rsa_sample():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    encrypted = public_key.encrypt(
        plaintext,
        rsa_pad.OAEP(
            mgf=rsa_pad.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open("samples/rsa_sample.enc", "wb") as f:
        f.write(encrypted)

    # Save private key for decryption
    with open("samples/rsa_private.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    print("[+] RSA sample + key created.")

def gen_xor_sample():
    key = 77  # XOR key
    encrypted = bytes([b ^ key for b in plaintext])
    with open("samples/xor_sample.enc", "wb") as f:
        f.write(encrypted)
    print("[+] XOR sample created (key = 77).")

def gen_base64_sample():
    encoded = base64.b64encode(plaintext)
    with open("samples/base64_sample.enc", "wb") as f:
        f.write(encoded)
    print("[+] Base64 sample created.")

# Run generators
gen_aes_sample()
gen_rsa_sample()
gen_xor_sample()
gen_base64_sample()

print("\n[✓] All sample encrypted files saved in ./samples/")
