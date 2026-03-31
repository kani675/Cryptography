from math import gcd

# Global variables
p = None
g = None
a = None
b = None
A = None
B = None
K = None

# Modular inverse function
def mod_inverse(k, p):
    for i in range(1, p):
        if (k * i) % p == 1:
            return i
    return None


def setup():
    global p, g, a, b
    print("\n===== DIFFIE-HELLMAN SETUP =====")

    p = int(input("Enter prime number p: "))
    g = int(input("Enter primitive root g: "))

    a = int(input("Enter Alice private key (a): "))
    b = int(input("Enter Bob private key (b): "))


def generate_public_keys():
    global p, g, a, b, A, B

    if None in (p, g, a, b):
        print("Complete setup first!")
        return

    print("\n===== GENERATING PUBLIC KEYS =====")

    A = pow(g, a, p)
    B = pow(g, b, p)

    print("Alice Public Key (A = g^a mod p) =", A)
    print("Bob Public Key   (B = g^b mod p) =", B)

    print("\n===== PUBLIC KEY DIRECTORY =====")
    print("Alice -> (p =", p, ", g =", g, ", A =", A, ")")
    print("Bob   -> (p =", p, ", g =", g, ", B =", B, ")")


def generate_shared_secret():
    global p, a, b, A, B, K

    if None in (A, B):
        print(" Generate public keys first!")
        return

    print("\n===== SHARED SECRET COMPUTATION =====")

    K_alice = pow(B, a, p)
    K_bob = pow(A, b, p)

    print("Alice computes K = B^a mod p =", K_alice)
    print("Bob computes   K = A^b mod p =", K_bob)

    K = K_alice
    print("Final Shared Secret Key (K) =", K)


def encrypt():
    global K, p

    if K is None:
        print("Generate shared secret first!")
        return

    print("\n===== ENCRYPTION =====")
    m = int(input("Enter message m: "))

    print("\nUsing Formula:")
    print("Y = Eeb(m) = (m * K) mod p")

    Y = (m * K) % p

    print("Y =", m, "*", K, "mod", p, "=", Y)


def decrypt():
    global K, p

    if K is None:
        print("Generate shared secret first!")
        return

    print("\n===== DECRYPTION =====")
    Y = int(input("Enter cipher Y: "))

    K_inv = mod_inverse(K, p)

    print("\nUsing Formula:")
    print("Ddb(Y) = (Y * K^-1) mod p")

    m = (Y * K_inv) % p

    print("m =", Y, "*", K_inv, "mod", p, "=", m)


# ===== MENU =====
while True:
    print("\n========== DIFFIE-HELLMAN MENU ==========")
    print("1. Setup Parameters")
    print("2. Generate Public Keys")
    print("3. Generate Shared Secret")
    print("4. Encrypt Message")
    print("5. Decrypt Message")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        setup()
    elif choice == 2:
        generate_public_keys()
    elif choice == 3:
        generate_shared_secret()
    elif choice == 4:
        encrypt()
    elif choice == 5:
        decrypt()
    elif choice == 6:
        print("Exiting Program...")
        break
    else:
        print("Invalid choice!")
