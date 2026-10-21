from math import comb

p = float(input("Probabilidade de defeito: "))
n = int(input("Tamanho do lote: "))
k = int(input("Quantidade exata de defeituosos (item b): "))
m = int(input("Mais de quantos defeituosos (item c): "))

pZero = comb(n, 0) * p**0 * (1 - p)**n
a = 1 - pZero

b = comb(n, k) * p**k * (1 - p)**(n - k)

soma = 0
for i in range(m + 1):
    soma = soma + comb(n, i) * p**i * (1 - p)**(n - i)
c = 1 - soma

esperado = n * p
bons = n * (1 - p)
var = n * p * (1 - p)

print("a) Algum item com defeito:", a)
print("b) Exatamente", k, "defeituosos:", b)
print("c) Mais de", m, "defeituosos:", c)
print("d) Esperado de defeituosos:", esperado)
print("d) Esperado de bons:", bons)
print("e) Variância:", var)