# ================= EUCLIDEAN ALGORITHM =================
def gcd_euclidean(a, b):
    steps = []
    step = 1

    steps.append("Using Formula:")
    steps.append("gcd(a, b) = gcd(b, a mod b)\n")

    while b != 0:
        r = a % b
        steps.append(f"Step {step}:")
        steps.append(f"gcd({a}, {b}) = gcd({b}, {a} mod {b})")
        steps.append(f"gcd({a}, {b}) = gcd({b}, {r})\n")
        a, b = b, r
        step += 1

    steps.append("Since remainder = 0")
    steps.append(f"GCD = {a}")

    return a, "\n".join(steps)


# ================= MENU DRIVER =================
print("EUCLIDEAN ALGORITHM - GCD\n")

a = int(input("Enter first positive integer (a): "))
b = int(input("Enter second positive integer (b): "))

if a <= 0 or b <= 0:
    print("Please enter positive integers only.")
else:
    gcd, steps = gcd_euclidean(a, b)
    print("\n--- Intermediate Steps ---")
    print(steps)