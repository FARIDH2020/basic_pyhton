# operator NOT
a = True
b = not a
print("data a = ", a)
print("--------NOT--------")
print("data b = ", b)

# operator AND
print("===== AND =====")
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)
a = False
b = True
c = a and b
print(a, "AND", b, " =", c)
a = True
b = False
c = a and b
print(a, " AND", b, "=", c)
a = True
b = True
c = a and b
print(a, " AND", b, " =", c)

# operator OR
print("===== OR =====")
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)
a = False
b = True
c = a or b
print(a, "OR", b, " =", c)
a = True
b = False
c = a or b
print(a, " OR", b, "=", c)
a = True
b = True
c = a or b
print(a, " OR", b, " =", c)

# operator XOR
print("===== XOR =====")
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, " =", c)
a = True
b = False
c = a ^ b
print(a, "XOR", b, " =", c)
a = True
b = True
c = a ^ b
print(a, "XOR", b, "  =", c)
