#Teste para saber se pode se aposentar ou não
idade=int(input("Nos informe a sua idade: "))
servico=int(input("Nos informe seu tempo de serviço, em anos: "))
if idade>=65:
    print("Você pode se aposentar!")
elif servico>=30:
    print("Você já trabalhou o suficiente, pode se aposentar!")
elif idade>=60 and servico>=25:
    print("Você já pode se aposentar!")
else:
    print("Você ainda não pode se aposentar: ")