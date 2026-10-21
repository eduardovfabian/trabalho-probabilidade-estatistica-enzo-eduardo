n = int(input("Quantidade de clientes: "))

p = []
e = []

for i in range(n):
    a = float(input(f"Probabilidade de o pedido vir do cliente {i + 1}: "))
    b = float(input(f"Probabilidade de erro do cliente {i + 1}: "))
    p.append(a)
    e.append(b)

probErro = 0
for i in range(n):
    probErro = probErro + p[i] * e[i]

print("a) Probabilidade de o sistema apresentar erro:", probErro)

k = int(input("Qual cliente você quer investigar (número)? "))

probCliente = p[k - 1] * e[k - 1] / probErro

print("b) Probabilidade de ser do cliente", k, "dado que houve erro:", probCliente)