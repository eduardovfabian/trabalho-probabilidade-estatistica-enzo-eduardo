pj = float(input("Probabilidade de Joãozinho resolver: "))
pm = float(input("Probabilidade de Mariazinha resolver: "))

probNao = (1 - pj) * (1 - pm)
prob = 1 - probNao

print("Probabilidade de o problema ser resolvido:", prob)