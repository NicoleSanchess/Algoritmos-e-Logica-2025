# Programa para cálculo de salário de vendedor

salario_fixo = float(input("Informe o valor do salário fixo: "))
comissao_produto = float(input("Infome o valor da comissão do produto: "))
quantidade_produtos = int(input("Informe o valor de produtos vendidos: "))

salario_total = salario_fixo + (comissao_produto * quantidade_produtos)

print(f"O valor do salário bruto é R$ {salario_total}")