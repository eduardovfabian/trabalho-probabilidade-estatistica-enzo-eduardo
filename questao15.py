import matplotlib.pyplot as plt

A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
D = float(input("D: "))


media = (A + B) / 2
variancia = (B - A) ** 2 / 12

inicio = max(C, A)
fim = min(D, B)
if fim > inicio:
    prob = (fim - inicio) / (B - A)
else:
    prob = 0

 
print("Valor esperado =", media)
print("Variância =", variancia)
print("P(C < X < D) =", prob)

altura = 1 / (B - A)

plt.plot([A, A, B, B], [0, altura, altura, 0])    
plt.fill_between([inicio, fim], [altura, altura])
plt.title("Distribuição Uniforms")
plt.show()