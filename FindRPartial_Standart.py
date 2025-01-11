#!pip install ecdsa

# Finding the K value that contains part of the R value (Standart)
SearchStartKvalue = 1
FindRPartial = 123

from ecdsa import SECP256k1

def CreateR(k: int):
    G = SECP256k1.generator
    n = SECP256k1.order
    P = k * G
    r = P.x() % n
    return r
    
def find_k_with_prefix(prefix, start_k):
    k = start_k
    while True:
        r = CreateR(k)
        r_hex = hex(r)[2:].upper()
        if r_hex.startswith(prefix):
        #if prefix in r_hex:
        #if r_hex.endswith(prefix):
            return k,r, r_hex
        k += 1

k,r, r_hex = find_k_with_prefix(FindRPartial, SearchStartKvalue)
print(f"Found K: {k}")
print(f"R: {r}")
print(f"R (hex): {r_hex}")
