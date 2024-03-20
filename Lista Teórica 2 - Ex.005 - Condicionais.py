#Calculando o peso ideal de uma pessoa
h=float(input("Qual a sua altura: \n"))
genero=str(input(f"Digite seu gênero: \n"))
gen1=("masculino")
gen2=("feminino"or"Feminino")
peso1=(72.7*h)-58
peso2=(62.1*h)-44.7
if genero=="masculino":
    print(f"Seu gênero é: {gen1}")
elif genero=="feminino":
    print(f"Seu gênero é: {gen2}")
#Calculando o Peso
if genero==gen1:
    print(format(f"Seu peso ideal seria: {peso1:.2f}"))
elif genero==gen2:
    print(format(f"Seu peso ideal seria: {peso2:.2f}"))