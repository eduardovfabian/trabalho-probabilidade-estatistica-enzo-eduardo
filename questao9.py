config = int(input("Configuração (1 ou 2): "))

p1 = float(input("Probabilidade de C1 funcionar: "))
p2 = float(input("Probabilidade de C2 funcionar: "))
p3 = float(input("Probabilidade de C3 funcionar: "))
p4 = float(input("Probabilidade de C4 funcionar: "))

if config == 1:
    r1 = p1 * p2
    r2 = p3 * p4
    prob = 1 - (1 - r1) * (1 - r2)
else:
    b1 = 1 - (1 - p1) * (1 - p3)
    b2 = 1 - (1 - p2) * (1 - p4)
    prob = b1 * b2

print("Probabilidade do sistema funcionar:", prob)