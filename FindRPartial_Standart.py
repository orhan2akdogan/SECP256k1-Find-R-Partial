#!pip install ecdsa

from ecdsa import SECP256k1

def CreateR(k: int):
    G = SECP256k1.generator
    n = SECP256k1.order
    P = k * G
    r = P.x() % n
    return r

def find_k_with_prefix(prefix="123", start_k=1):
    k = start_k
    while True:
        r = CreateR(k)
        r_hex = hex(r)[2:].upper()
        if r_hex.startswith(prefix):
        #if prefix in r_hex:
        #if r_hex.endswith(prefix):
            return k, r_hex
        k += 1

k, r_hex = find_k_with_prefix()
print(f"Found k: {k}")
print(f"R(HEX): {r_hex}")
