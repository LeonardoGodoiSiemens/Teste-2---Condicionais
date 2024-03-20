#Criando a Bhaskara com Python
a=float(input("DIGITE AQUI O VALOR DE a, o qual não pode ser zero: "))
b=float(input("DIGITE AQUI O VALOR DE b: "))
c=float(input("DIGITE AQUI O VALOR DE c: "))
delta= (b**2) - 4*a*c
if delta==0:
    print(f"Como delta é: {delta}, Existem duas raízes reais e iguais")
elif delta>0:
    print(f"Como delta é: {delta}, Existem duas raízes reais e diferentes")
else:
    print(f"Como delta é: {delta}, Existem duas raízes imaginárias")