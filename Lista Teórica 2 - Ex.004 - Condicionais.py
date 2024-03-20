#Lendo a Nota do Estudante
nota=float(input("Qual foi a sua nota: "))
if nota>=7:
    print("Estudante aprovado!")
elif nota >=4 and nota<7:
    print("Estudante em Recuperação!")
else:
    print("Estudante repovado!")