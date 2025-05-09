while True:
    operation = input('Digite a opção desejada: \n 1. Calcular IR (Imposto de Renda) \n')
    if operation == '1':
        break

print('-' * 50)

salario_input = input('Digite seu salário bruto: R$ ').replace(",", ".")
print('-' * 50)

try:
    salario = float(salario_input)

    if salario <= 2428.80:
        aliquota = 0
    elif salario <= 2826.65:
        aliquota = 7.5
    elif salario <= 3751.05:
        aliquota = 15.0
    elif salario <= 4664.68:
        aliquota = 22.5
    else:
        aliquota = 27.5

    desconto = salario * (aliquota / 100)
    liquido = salario - desconto

    print('Resultado do cálculo de IR:')
    print(f"Salário Bruto: R$ {salario:.2f}")
    print(f"Alíquota Aplicada: {aliquota}%")
    print(f"Desconto IR: R$ {desconto:.2f}")
    print(f"Salário Líquido: R$ {liquido:.2f}")

except ValueError:
    print('Entrada inválida. Digite um número válido para o salário.')

print('-' * 50)
