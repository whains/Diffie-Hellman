import gensafeprime
from random import SystemRandom

bitNum = 512

p = gensafeprime.generate(bitNum)
a = SystemRandom().getrandbits(bitNum)

print("p")
print(p)

print("a")
print(a)
