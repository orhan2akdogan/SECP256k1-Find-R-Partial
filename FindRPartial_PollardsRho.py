#!pip install ecdsa

# Finding the K value that contains part of the R value (Pollards Rho)
SearchStartKvalue = 97550250915353978318189854416261922300439940533550735609205232015416706969856
FindRPartial = "222"

from ecdsa import SECP256k1

def CreateR(k: int):
    G = SECP256k1.generator
    n = SECP256k1.order
    P = k * G
    r = P.x() % n
    return r

def pollards_rho_with_prefix(pFindRPartial="", pSearchStartKvalue=1):
    def f(x):
      return (x*x + 1) % SECP256k1.order

    tortoise = pSearchStartKvalue
    hare = pSearchStartKvalue

    while True:
        tortoise = f(tortoise)
        hare = f(f(hare))

        r_tortoise = CreateR(tortoise)
        r_hare = CreateR(hare)

        r_hex_tortoise = hex(r_tortoise)[2:].upper()
        r_hex_hare = hex(r_hare)[2:].upper()

        #if prefix in r_hex_tortoise:
        if r_hex_tortoise.startswith(pFindRPartial):
             return tortoise,r_tortoise, r_hex_tortoise

        #if prefix in r_hex_hare:
        if r_hex_hare.startswith(pFindRPartial):
            return hare, r_hare, r_hex_hare

        if tortoise == hare:
             return None, None

k,r, r_hex = pollards_rho_with_prefix(FindRPartial, SearchStartKvalue)

print(f"Found K: {k}")
print(f"R: {r}")
print(f"R (hex): {r_hex}")

