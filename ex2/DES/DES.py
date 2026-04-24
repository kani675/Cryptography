# ===== S-DES (Single Round, NO P4) =====

# ---- TABLES ----
P10 = [3,5,2,7,4,10,1,9,8,6]
P8  = [6,3,7,4,8,5,10,9]
IP  = [2,6,3,1,4,8,5,7]
IP_INV = [4,1,3,5,7,2,8,6]
EP  = [4,1,2,3,2,3,4,1]

S0 = [
    [1,0,3,2],
    [3,2,1,0],
    [0,2,1,3],
    [3,1,3,2]
]

S1 = [
    [0,1,2,3],
    [2,0,1,3],
    [3,0,1,0],
    [2,1,0,3]
]

# ---- COMMON FUNCTIONS ----
def permute(bits, table):
    return "".join(bits[i-1] for i in table)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(a, b):
    return "".join(str(int(x)^int(y)) for x,y in zip(a,b))

def swap(bits):
    return bits[4:] + bits[:4]

def sbox(bits, box):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(box[row][col], "02b")

# ---- KEY GENERATION (ONLY K1) ----
def generate_k1(key):
    print("\n--- KEY GENERATION ---")
    print("Original Key:", key)

    p10 = permute(key, P10)
    print("After P10:", p10)

    L, R = p10[:5], p10[5:]
    L = left_shift(L, 1)
    R = left_shift(R, 1)
    print("After LS-1 → L:", L, "R:", R)

    k1 = permute(L + R, P8)
    print("Generated K1:", k1)
    return k1

# ---- fK FUNCTION (NO P4) ----
def fk(bits, key):
    L, R = bits[:4], bits[4:]
    print("L =", L, "R =", R)

    ep = permute(R, EP)
    print("EP(R):", ep)

    x = xor(ep, key)
    print("EP ⊕ K1:", x)

    s0 = sbox(x[:4], S0)
    s1 = sbox(x[4:], S1)
    print("S0 Output:", s0)
    print("S1 Output:", s1)

    R1 = xor(L, s0 + s1)
    L1 = R
    print("L1 =", L1)
    print("R1 =", R1)

    return L1 + R1

# ---- ENCRYPT ----
def encrypt():
    pt = input("Enter 8-bit Plain Text: ")
    key = input("Enter 10-bit Key: ")

    print("\n=== S-DES ENCRYPTION ===")
    k1 = generate_k1(key)

    ip = permute(pt, IP)
    print("\nAfter IP:", ip)

    r = fk(ip, k1)

    ct = permute(r, IP_INV)
    print("\nAfter IP⁻¹:", ct)
    print("\nCipher Text:", ct)

# ---- DECRYPT ----
def decrypt():
    ct = input("Enter 8-bit Cipher Text: ")
    key = input("Enter 10-bit Key: ")

    print("\n=== S-DES DECRYPTION ===")
    k1 = generate_k1(key)

    ip = permute(ct, IP)
    print("\nAfter IP:", ip)

    sw = swap(ip)
    print("After SWAP:", sw)

    r = fk(sw, k1)

    pt = permute(r, IP_INV)
    print("\nAfter IP⁻¹:", pt)
    print("\nPlain Text:", pt)

# ---- MENU DRIVER ----
while True:
    print("\n====== S-DES MENU ======")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        encrypt()
    elif choice == "2":
        decrypt()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")