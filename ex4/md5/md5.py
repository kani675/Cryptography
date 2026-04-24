# MD5 Full Step-by-Step Implementation (Verbose)

import math

MASK = 0xFFFFFFFF

# Shift amounts
S = [
    7,12,17,22, 7,12,17,22, 7,12,17,22, 7,12,17,22,
    5,9,14,20, 5,9,14,20, 5,9,14,20, 5,9,14,20,
    4,11,16,23, 4,11,16,23, 4,11,16,23, 4,11,16,23,
    6,10,15,21, 6,10,15,21, 6,10,15,21, 6,10,15,21
]

# Constants (T table)
K = [int((1 << 32) * abs(math.sin(i + 1))) & MASK for i in range(64)]

def left_rotate(x, c):
    return ((x << c) | (x >> (32 - c))) & MASK


def md5_verbose(message):
    msg = bytearray(message, 'utf-8')

    print("Original Message:", message)
    print("ASCII Bytes:", list(msg))

    # Padding
    bit_len = (len(msg) * 8) & 0xffffffffffffffff
    msg.append(0x80)

    while (len(msg) % 64) != 56:
        msg.append(0)

    msg += bit_len.to_bytes(8, 'little')

    print("\nAfter Padding Length:", len(msg))

    # Initial Hash Values
    A = 0x67452301
    B = 0xefcdab89
    C = 0x98badcfe
    D = 0x10325476
    count =0

    # Process 512-bit blocks
    for offset in range(0, len(msg), 64):
        print("\n==============================")
        print("Processing Block:", offset)
        print("==============================")

        block = msg[offset:offset+64]

        # Break into 16 words
        M = []
        for i in range(16):
            val = int.from_bytes(block[i*4:(i+1)*4], 'little')
            M.append(val)

        a, b, c, d = A, B, C, D

        print("\n--- Initial Values ---")
        print(f"a={a:08x} b={b:08x} c={c:08x} d={d:08x}")

        print("\n--- 64 Rounds ---")

        for i in range(64):

            if i < 16:
                f = (b & c) | (~b & d)
                g = i
            elif i < 32:
                f = (d & b) | (~d & c)
                g = (5*i + 1) % 16
            elif i < 48:
                f = b ^ c ^ d
                g = (3*i + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7*i) % 16

            f = (f + a + K[i] + M[g]) & MASK

            a = d
            d = c
            c = b
            b = (b + left_rotate(f, S[i])) & MASK
            if(i<3 or i>61):
                print(f"\nRound {i}")
                print(f"a={a:08x} b={b:08x} c={c:08x} d={d:08x}")
                print(f"f={f:08x} K={K[i]:08x} M[g]={M[g]:08x}")
            elif(count==0):
                print("\n\nSkiping some rounds ...\n")
                count+=1
        # Add to hash
        A = (A + a) & MASK
        B = (B + b) & MASK
        C = (C + c) & MASK
        D = (D + d) & MASK

        print("\n--- Updated Hash ---")
        print(f"A={A:08x} B={B:08x} C={C:08x} D={D:08x}")

    # Final hash (little-endian)
    final_hash = ''.join(x.to_bytes(4, 'little').hex() for x in [A, B, C, D])

    print("\n==============================")
    print("FINAL MD5 HASH:")
    print(final_hash)

    return final_hash


# Run
if __name__ == "__main__":
    text = input("Enter text: ")
    md5_verbose(text)