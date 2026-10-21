estados=[]
for A in [True,False]:
    for B in [True,False]:
        estados.append((A,B))

def expressao_1(A,B):
    return A and not B

def expressao_2(A,B):
    return not(A and B)

def expressao_3(A,B):  
    return A and not B  

def expressao_4(A,B):
   return not A or not B



def regra_a(A,B):
    return A and not B

def regra_b(A,B):
    return not(A and B)

#-------------------------------QUESTAO 1----------------------------------#
sao_iguais_1=True
for A,B in estados:
    if expressao_1(A,B) != regra_a(A,B):
        sao_iguais_1=False
        break
if sao_iguais_1:
    print("A expressao 1 esta correta para a questao 1")

#-------------------------------------------------------------------------#

sao_iguais_2=True
for A,B in estados:
    if expressao_2(A,B) != regra_a(A,B):
        sao_iguais_2=False
        break
if sao_iguais_2:
    print("A expressao 2 esta correta para a questao 1")

#-------------------------------------------------------------------------#

sao_iguais_3=True
for A,B in estados:
    if expressao_3(A,B) != regra_a(A,B):
        sao_iguais_3=False
        break
if sao_iguais_3:
    print("A expressao 3 esta correta para a questao 1")

#-------------------------------------------------------------------------#

sao_iguais_4=True
for A,B in estados:
    if expressao_4(A,B) != regra_a(A,B):
        sao_iguais_4=False
        break
if sao_iguais_4:
    print("A expressao 4 esta correta para a questao 1")

#-------------------------------QUESTAO 2----------------------------------#
sao_iguais_5=True
for A,B in estados:
    if expressao_1(A,B) != regra_b(A,B):
        sao_iguais_5=False
        break
if sao_iguais_5:
    print("A expressao 1 esta correta para a questao 2")

#-------------------------------------------------------------------------#

sao_iguais_6=True
for A,B in estados:
    if expressao_2(A,B) != regra_b(A,B):
        sao_iguais_6=False
        break
if sao_iguais_6:
    print("A expressao 2 esta correta para a questao 2")

#-------------------------------------------------------------------------#

sao_iguais_7=True
for A,B in estados:
    if expressao_3(A,B) != regra_b(A,B):
        sao_iguais_7=False
        break
if sao_iguais_7:
    print("A expressao 3 esta correta para a questao 2")

#-------------------------------------------------------------------------#

sao_iguais_8=True
for A,B in estados:
    if expressao_4(A,B) != regra_b(A,B):
        sao_iguais_8=False
        break
if sao_iguais_8:
    print("A expressao 4 esta correta para a questao 2")

