import math

def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

M1 = float(input("Média de X1: "))
D1 = float(input("Desvio-padrão de X1: "))
M2 = float(input("Média de X2: "))
D2 = float(input("Desvio-padrão de X2: "))

media = M1 + M2
desvio = math.sqrt(D1 ** 2 + D2 ** 2)

MS = float(input("MS: "))
z = (MS - media) / desvio
probA = 1 - phi(z)

I1 = float(input("I1: "))
I2 = float(input("I2: "))
z1 = (I1 - media) / desvio
z2 = (I2 - media) / desvio
probB = phi(z2) - phi(z1)

print(f"a) {probA}")
print(f"b) {probB}")