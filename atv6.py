engenharia_civil=int(input("Quantidade de alunos em engenharia civil - "))
engenharias=int(input("Quantidade de alunos em outras engenharias - "))

total_estudantes=engenharia_civil+engenharias

def calcular_prob (civil, total, n):
    probablidade=1
    for i in range(n):
        probablidade *=(civil-i)/(total-i)
    return probablidade
questao_a=calcular_prob(engenharia_civil,total_estudantes,2)
questao_b=calcular_prob(engenharia_civil,total_estudantes,4)

print(f"{questao_a * 100: .2f}%")
print(f"{questao_b * 100: .2f}%")
