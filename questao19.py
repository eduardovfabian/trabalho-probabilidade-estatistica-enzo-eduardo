import math


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


Me = float(input("Media: "))
Dp = float(input("Desvio-padrao: "))


I1 = float(input("I1: "))
I2 = float(input("I2: "))
z1 = (I1 - Me) / Dp
z2 = (I2 - Me) / Dp
probA = phi(z2) - phi(z1)


MA = float(input("MA: "))
z = (MA - Me) / Dp
probB = 1 - phi(z)


ME = float(input("ME: "))
z = (ME - Me) / Dp
probC = phi(z)

print(f"a) {probA}")
print(f"b) {probB}")
print(f"c) {probC}")