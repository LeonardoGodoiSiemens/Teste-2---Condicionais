#Notas bimestrais analise
cod1="1"
cod2="2"
uni=str(input("Responda 1 se você estudou na PUCPR, e 2 caso tenha estudado na UNICAMP: \n"))
#Teste
if uni==cod1:
    print("Você estudou na PUCPR!")
    nota=float(input("Qual a sua nota: \n"))
    if nota>=7:
        print("Você está aprovado!")
    elif nota<4:
        print("Você está reprovado!")
    else:
        print("Você está em Exame/Recuperação")
elif uni==cod2:
    print("Você estudou na UNICAMP!")
    nota=float(input("Qual a sua nota: \n"))
    if nota>=5:
        print("Você está aprovado!")
    elif nota<5:
        print("Você está em Exame/Recuperação")
else:
    print("Você nnão estuda em nenhuma das Universidades do formulário!")