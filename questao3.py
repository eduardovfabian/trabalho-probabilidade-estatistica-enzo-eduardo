n = int(input("Quantidade de empresas: "))

funcionarios = []  

for i in range(n):
    qtd = int(input(f"Funcionários da empresa {i + 1}: "))
    funcionarios.append(qtd)

total = sum(funcionarios)

# a) 
for i in range(n):
    prob = funcionarios[i] / total
    print(f"Empresa {i + 1}: {prob}")

# b)
prob_nao = 1 - funcionarios[0] / total
print(f"Empresa 1 não ser selecionada: {prob_nao}")