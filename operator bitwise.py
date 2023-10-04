a = 4
b = 6


# bitwise "OR" (|)
c = a | b
print("\n=======OR=======")
print("nilai:", a, "binary:", format(a, "08b"))
print("nilai:", b, "binary:", format(b, "08b"))
print("--------------------- (|)")
print("nilai:", c, "binary:", format(c, "08b"))

# bitwise "AND" (&)
c = a & b
print("\n=======AND======")
print("nilai:", a, "binary:", format(a, "08b"))
print("nilai:", b, "binary:", format(b, "08b"))
print("--------------------- (&)")
print("nilai:", c, "binary:", format(c, "08b"))

# bitwise "XOR" (^)
c = a ^ b
print("\n=======XOR======")
print("nilai:", a, "binary:", format(a, "08b"))
print("nilai:", b, "binary:", format(b, "08b"))
print("--------------------- (^)")
print("nilai:", c, "binary:", format(c, "08b"))

# bitwise "NOT" (~)
c = ~a
print("\n=======XOR======")
print("nilai:", a, "binary:", format(a, "08b"))
print("nilai:", b, "binary:", format(b, "08b"))
print("--------------------- (~)")
print("nilai:", c, "binary:", format(c, "08b"))
print("--------------------------(^)")
d = 0b00001000
e = 0b11111111
print("nilai:", e ^ d, "binary:", format(d ^ e, "08b"))

# bitwise "SHIFT RIGHT" (>>)
c = a >> 1
d = b >> 1
print("\n=======>>=======")
print("nilai:", a, "binary:", format(a, "08b"))
print("nilai:", b, "binary:", format(b, "08b"))
print("--------------------- (>>)")
print("nilai:", c, "binary:", format(c, "08b"))
print("nilai:", d, "binary:", format(d, "08b"))

# bitwise "SHIFT LEFT" (<<)
c = a << 1
d = b << 1
print("\n=======>>=======")
print("nilai:", a, "binary:", format(a, "08b"))
print("nilai:", b, "binary:", format(b, "08b"))
print("--------------------- (<<)")
print("nilai:", c, "binary:", format(c, "08b"))
print("nilai:", d, "binary:", format(d, "08b"))
