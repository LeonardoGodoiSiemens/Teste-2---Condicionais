#Teste para saber que tipo de eleitor você é!
eleitor=int(input("Nos informe a sua idade: "))
if eleitor<16:
    print("Você ainda não é um eleitor!")
elif eleitor==16 or eleitor ==17 or eleitor<18 or eleitor>65:
    print("Você é um eleitor facultativo!")
else:
    print("Você é um eleitor obrigatório!")