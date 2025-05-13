print("""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$                                               $ 
$                                               $  
$         Calculadora de desconto de IR         $
$                                               $ 
$                                               $ 
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
""")

controle = True
while controle:
    leitura = input("Informe o salário: R$").replace(",",".")
    try:
        salario = float(leitura)
        controle = False

    except ValueError:
        print("Entrada inválida! Tente novamente.\n")

desconto = 0

if salario <= 2428.80:
      print("Não possui desconto de IR")
elif salario <= 2826.65:
      desconto = (salario * (7.5/100))
elif salario <= 3751.05:
      desconto = (salario * (15/100))
elif salario <= 4664.68:
     desconto = (salario * (22.5/100))
else:
     desconto = (salario * (27.5/100))

salario = salario - desconto
print(f"Valor do desconto de IR: R${desconto:.2f}")
print(f"Salário líquido: R${salario:.2f}")
