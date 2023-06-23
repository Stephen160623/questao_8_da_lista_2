t1 = int(input("Sua nota no teste 1: "))
t2 = int(input("Sua nota no teste 2: "))
pf = int(input("Sua nota na prova: "))

nota = round((t1*0.15+t2*0.15+0.7*pf), 3)

if nota >= 6:
    print("APROVADO")
else:
    rec = int(input("Qual foi sua nota na recuperação: "))
    nota2 = round((rec*2+nota*3)/5,3)
    if nota2 >= 6:
        print("APROVADO")
    else:
        print("REPROVADO")