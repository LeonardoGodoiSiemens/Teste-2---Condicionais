#Separando os números pares e ímpares
numero=int(input("Digite um número inteiro: "))
if numero %2==0:
    print("O número é P")
else:
    print("O número é I")
print(f"Seu número é {numero}")