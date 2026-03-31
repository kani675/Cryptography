# ================= CAESAR CIPHER =================
def caesar(text, encrypt=True):
    shift = 3 if encrypt else 23
    result = ""
    steps = "Shift = 3\n\n"

    for c in text:
        v = ord(c) - 65
        nv = (v + shift) % 26
        nc = chr(nv + 65)
        steps += f"{c} -> ({v}+3)%26 = {nv} -> {nc}\n"
        result += nc

    return result, steps


# ================= PLAYFAIR CIPHER =================
def create_matrix(key):
    key = key.replace("J", "I")
    alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    s = ""
    for c in key + alpha:
        if c not in s:
            s += c
    return [list(s[i*5:(i+1)*5]) for i in range(5)]

def find(c, m):
    for i in range(5):
        for j in range(5):
            if m[i][j] == c:
                return i, j

def playfair(text, key, encrypt=True):
    text = text.replace("J", "I")
    processed, i = "", 0

    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"
        if a == b:
            processed += a + "X"
            i += 1
        else:
            processed += a + b
            i += 2

    if len(processed) % 2 != 0:
        processed += "X"

    matrix = create_matrix(key)
    shift = 1 if encrypt else -1
    result = ""
    steps = "Playfair Matrix:\n"

    for r in matrix:
        steps += " ".join(r) + "\n"

    steps += "\nDigraph Steps:\n"

    for i in range(0, len(processed), 2):
        a, b = processed[i], processed[i+1]
        r1, c1 = find(a, matrix)
        r2, c2 = find(b, matrix)

        if r1 == r2:
            x = matrix[r1][(c1 + shift) % 5]
            y = matrix[r2][(c2 + shift) % 5]
        elif c1 == c2:
            x = matrix[(r1 + shift) % 5][c1]
            y = matrix[(r2 + shift) % 5][c2]
        else:
            x = matrix[r1][c2]
            y = matrix[r2][c1]

        result += x + y
        steps += f"{a}{b} -> ({r1},{c1}) ({r2},{c2}) -> {x}{y}\n"

    return result, steps


# ================= HILL CIPHER =================
def mod_inv(a):
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            return i
    return None

def inverse_matrix(m):
    a, b, c, d = m
    det = (a*d - b*c) % 26
    inv = mod_inv(det)
    if inv is None:
        return None
    return [(d*inv)%26, (-b*inv)%26, (-c*inv)%26, (a*inv)%26]

def hill(text, key, encrypt=True):
    m = list(map(int, key.split()))

    if not encrypt:
        m = inverse_matrix(m)
        if not m:
            return "", "Matrix not invertible"

    if len(text) % 2 != 0:
        text += "X"

    result = ""
    steps = "Matrix:\n"
    steps += f"{m[0]} {m[1]}\n{m[2]} {m[3]}\n\n"

    for i in range(0, len(text), 2):
        x1 = ord(text[i]) - 65
        x2 = ord(text[i+1]) - 65
        y1 = (m[0]*x1 + m[1]*x2) % 26
        y2 = (m[2]*x1 + m[3]*x2) % 26

        c1 = chr(y1 + 65)
        c2 = chr(y2 + 65)

        steps += f"{text[i]}{text[i+1]} -> ({x1},{x2}) -> ({y1},{y2}) -> {c1}{c2}\n"
        result += c1 + c2

    return result, steps


# ================= MENU DRIVER =================
while True:
    print("\n--- SUBSTITUTION CIPHER MENU ---")
    print("1. Caesar Cipher")
    print("2. Playfair Cipher")
    print("3. Hill Cipher")
    print("4. Exit")

    choice = input("Choose Cipher: ")

    if choice == "4":
        print("Program Ended")
        break

    print("\n1. Encrypt")
    print("2. Decrypt")
    mode = input("Choose Operation: ")
    encrypt = True if mode == "1" else False

    if choice == "1":
        text = input("Enter Plain Text: ").upper().replace(" ", "")
        result, steps = caesar(text, encrypt)

    elif choice == "2":
        text = input("Enter Plain Text: ").upper().replace(" ", "")
        key = input("Enter Key: ").upper().replace(" ", "")
        result, steps = playfair(text, key, encrypt)

    elif choice == "3":
        text = input("Enter Plain Text: ").upper().replace(" ", "")
        key = input("Enter 2x2 Matrix (a b c d): ")
        result, steps = hill(text, key, encrypt)

    else:
        print("Invalid Choice")
        continue

    print("\nResult:", result)
    print("\n--- Intermediate Steps ---")
    print(steps)