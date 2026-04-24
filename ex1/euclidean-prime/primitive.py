# ================= POWER MOD =================
def power_mod(base, exp, mod):
    result = 1
    for _ in range(exp):
        result = (result * base) % mod
    return result


# ================= CHECK PRIMITIVE ROOT =================
def is_primitive_root(g, p):
    phi = p - 1
    values = set()
    steps = ""

    for k in range(1, phi + 1):
        val = power_mod(g, k, p)
        values.add(val)
        steps += f"{g}^{k} mod {p} = {val}\n"

    return len(values) == phi, steps


# ================= FIND FIRST PRIMITIVE ROOT =================
def find_first_primitive_root(p):
    output = ""

    for g in range(2, p):
        output += f"Trying g = {g}\n"
        is_root, steps = is_primitive_root(g, p)
        output += steps

        if is_root:
            output += f"\nFirst primitive root of {p} is {g}"
            return output

        output += f"{g} is NOT a primitive root\n\n"

    return "No primitive root found."


# ================= MENU DRIVER =================
print("PRIMITIVE ROOT PROGRAM\n")

p = int(input("Enter a prime number (p): "))
if p <= 1:
    print("Invalid prime number")
    exit()

print(f"\nφ({p}) = {p - 1}\n")

print("1. Check whether g is a primitive root of p")
print("2. Find first primitive root of p")
choice = input("Enter choice: ")

if choice == "1":
    g = int(input("Enter g: "))
    result, steps = is_primitive_root(g, p)
    print("\n--- Steps ---")
    print(steps)

    if result:
        print(f"{g} IS a primitive root of {p}")
    else:
        print(f"{g} is NOT a primitive root of {p}")

elif choice == "2":
    print("\n--- Steps ---")
    print(find_first_primitive_root(p))

else:
    print("Invalid choice")