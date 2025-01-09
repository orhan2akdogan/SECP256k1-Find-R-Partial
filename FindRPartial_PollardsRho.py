from ecdsa import SECP256k1

prefix = "222"
start_k = 97550250915353978318189854416261922300439940533550735609205232015416706969856

def CreateR(k: int):
    G = SECP256k1.generator
    n = SECP256k1.order
    P = k * G
    r = P.x() % n
    return r

def pollards_rho_with_prefix(prefix, start_k=1):
    def f(x):
      return (x*x + 1) % SECP256k1.order

    tortoise = start_k
    hare = start_k

    while True:
        tortoise = f(tortoise)
        hare = f(f(hare))

        r_tortoise = CreateR(tortoise)
        r_hare = CreateR(hare)

        r_hex_tortoise = hex(r_tortoise)[2:].upper()
        r_hex_hare = hex(r_hare)[2:].upper()

        #if prefix in r_hex_tortoise:
        if r_hex_tortoise.startswith(prefix):
             return tortoise, r_hex_tortoise

        #if prefix in r_hex_hare:
        if r_hex_hare.startswith(prefix):
            return hare, r_hex_hare

        if tortoise == hare:
             return None, None

k, r_hex = pollards_rho_with_prefix(prefix, start_k)

if k:
    print(f"Found k: {k}")
    print(f"R(HEX): {r_hex}")
else:
    print("k not found")
