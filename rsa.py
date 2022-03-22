import gensafeprime

bitNum = 512

p = gensafeprime.generate(bitNum)
print("p")
print(p)

q = gensafeprime.generate(bitNum)
print("q")
print(q)

n = p * q
print("n")
print(n)

phiN = (p - 1) * (q - 1)

e = 65537


def modulo(g, a, p):
    result = 1
    while a != 0:
        if a & 0x01:
            result = result * g % p
        a = a >> 1
        g = g * g % p
    return result


def extendedEuclidian(a, b):
    s1 = 1
    s2 = 0
    while b != 0:
        q = a // b
        temp = a % b
        a = b
        b = temp
        s = s1 - q * s2
        s1 = s2
        s2 = s
    return s1


d = extendedEuclidian(e, phiN)
if d < 0:
    d += phiN

print("d")
print(d)

# Put in what auto grader gives here
m = 0
print("encrypt")
print(modulo(m, e, n))

# Put in what auto grader gives here
m = 0
print("decrypt")
print(modulo(m, d, n))

