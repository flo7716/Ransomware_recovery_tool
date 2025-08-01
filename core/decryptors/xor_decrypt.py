def bruteforce(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    print("[*] Attempting XOR brute-force decryption (1-byte key)...")

    for key in range(256):
        decrypted = bytes([b ^ key for b in data])
        if b"flag" in decrypted or b"password" in decrypted or b"http" in decrypted:
            out_path = file_path + f".xor_key_{key}.txt"
            with open(out_path, "wb") as out:
                out.write(decrypted)
            print(f"[+] Possible XOR decryption found with key {key}: {out_path}")
            return out_path