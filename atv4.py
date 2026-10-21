empresaA = int(input("qual o numero de funcionarios da empresa A:"))
empresaB = int(input("qual o numero de funcionarios da empresa B:"))
empresaC = int(input("qual o numero de funcionarios da empresa C:"))
empresaD = int(input("qual o numero de funcionarios da empresa D:"))
empresaE = int(input("qual o numero de funcionarios da empresa E:")) 

soma_total= empresaA+empresaB+empresaC+empresaD+empresaE

empresas=[empresaA, empresaB, empresaC, empresaD, empresaE]
nome=["A", "B", "C", "D", "E"]
for nome, funcionarios in zip(nome, empresas):
    probalidade= funcionarios/soma_total
    print(f"A probabliade de {nome} é {probalidade * 100:.2f}")

prob_nao_A = 1 - empresaA/soma_total
print(f"A probabilidade da empresa A n ser selecionada é de {prob_nao_A}")