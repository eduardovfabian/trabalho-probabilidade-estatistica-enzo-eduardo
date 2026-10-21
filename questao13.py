from math import exp, factorial

taxa = float(input("Taxa média de chegadas por minuto: "))
k1 = int(input("Quantidade de chegadas (item a): "))
t1 = float(input("Tempo em minutos (item a): "))
k2 = int(input("Quantidade de chegadas (item b): "))
t2 = float(input("Tempo em segundos (item b): "))

l1 = taxa * t1
a = exp(-l1) * l1**k1 / factorial(k1)

l2 = taxa * t2 / 60
b = exp(-l2) * l2**k2 / factorial(k2)

print("a) Probabilidade de", k1, "chegadas em", t1, "minuto(s):", a)
print("b) Probabilidade de", k2, "chegadas em", t2, "segundos:", b)