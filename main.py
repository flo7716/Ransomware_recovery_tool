from core.analyzer import analyze_file
from core.decryptors import aes_decrypt, rsa_decrypt, xor_decrypt, base64_decode

def main():
    filepath = input("Enter path to encrypted file: ").strip()
    algo = analyze_file(filepath)

    if algo == "AES":
        aes_decrypt.decrypt(filepath)
    elif algo == "RSA":
        rsa_decrypt.decrypt(filepath)
    elif algo == "XOR":
        xor_decrypt.bruteforce(filepath)
    elif algo == "BASE64":
        base64_decode.decode(filepath)
    else:
        print("[-] Unknown or unsupported encryption. Entropy or format too high.")

if __name__ == "__main__":
    main()
