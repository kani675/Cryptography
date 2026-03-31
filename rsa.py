from math import gcd

# Global variables to store keys
n = None
e = None
d = None

# Extended Euclidean Algorithm
def mod_inverse(e, phi):
    t, new_t = 0, 1
    r, new_r = phi, e

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        return None
    if t < 0:
        t = t + phi

    return t


def generate_keys():
    global n, e, d

    print("\n===== RSA KEY GENERATION =====")

    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))

    print("\nStep 1: p =", p, ", q =", q)

    # Step 2
    n = p * q
    print("Step 2: n = p * q =", n)

    # Step 3
    phi = (p - 1) * (q - 1)
    print("Step 3: phi(n) = (p-1)(q-1) =", phi)

    # Step 4
    e = int(input("Enter public exponent e: "))
    print("Checking gcd(e, phi(n))...")

    if gcd(e, phi) != 1:
        print("Invalid e. It must be coprime with phi(n).")
        return

    print("e is valid")

    # Step 5
    d = mod_inverse(e, phi)
    print("Step 5: d Concruent e^-1 mod phi(n)")
    print("d =", d)
    print("Verification: (e * d) mod phi(n) =", (e * d) % phi)

    print("\nPublic Key (n, e) =", (n, e))
    print("Private Key (d) =", d)


def encrypt():
    global n, e

    if n is None or e is None:
        print("Generate keys first!")
        return

    print("\n===== RSA ENCRYPTION =====")
    m = int(input("Enter message m: "))

    print("Formula: C = m^e mod n")
    C = pow(m, e, n)

    print("C =", m, "^", e, "mod", n, "=", C)


def decrypt():
    global n, d

    if n is None or d is None:
        print("Generate keys first!")
        return

    print("\n===== RSA DECRYPTION =====")
    C = int(input("Enter cipher text C: "))

    print("Formula: m = C^d mod n")
    m = pow(C, d, n)

    print("m =", C, "^", d, "mod", n, "=", m)


# ===== MENU DRIVER =====
while True:
    print("\n========== RSA MENU ==========")
    print("1. Generate Keys")
    print("2. Encrypt")
    print("3. Decrypt")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        generate_keys()
    elif choice == 2:
        encrypt()
    elif choice == 3:
        decrypt()
    elif choice == 4:
        print("Exiting RSA Program...")
        break
    else:
        print("Invalid choice! Try again.")
