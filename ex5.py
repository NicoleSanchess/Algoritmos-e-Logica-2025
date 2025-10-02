# Crie um programa que leia do usuário o salário (float)

salario = float(input("Informe o valor do salario: "))

if salario < 5000:
    imposto = salario * 0.18
else: 
    imposto = salario* 0.27

print (f"De acordo com o seu salário o valor do imposto é: {imposto}")
