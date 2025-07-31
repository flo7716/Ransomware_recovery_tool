import math
import os

def calculate_entropy(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()

    if not data:
        return 0

    byte_counts = [0] * 256
    for b in data:
        byte_counts[b] += 1

    entropy = 0
    for count in byte_counts:
        if count:
            p = count / len(data)
            entropy -= p * math.log2(p)
    return entropy

def read_file_bytes(path):
    with open(path, "rb") as f:
        return f.read()

def write_file_bytes(path, data):
    with open(path, "wb") as f:
        f.write(data)
    print(f"[+] Data written to {path}")