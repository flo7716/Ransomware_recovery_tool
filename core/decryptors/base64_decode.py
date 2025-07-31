import base64

def decode(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    try:
        decoded = base64.b64decode(data)
        out_path = file_path.replace(".enc", "") + ".b64_decoded.txt"
        with open(out_path, "wb") as f:
            f.write(decoded)
        print(f"[+] Base64 decoded to: {out_path}")
    except Exception as e:
        print("[-] Base64 decode failed:", e)
