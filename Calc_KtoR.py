#!pip install ecdsa

#Calc K to R
k = 33323733858381188570392591352545647629864124191588660716446995316358937866538

from ecdsa import SECP256k1

def CreateR(k: int):
    return (k * SECP256k1.generator).x() % SECP256k1.order
    
r = CreateR(k)
r_hex = hex(r)[2:].upper()

print(f"K: {k}")
print(f"R: {r}")
print(f"R (hex): {r_hex}")
