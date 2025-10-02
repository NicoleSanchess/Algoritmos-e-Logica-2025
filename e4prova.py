# Nicole Carolina Sanches
# RA: 0220482523004
# Avaliação Algoritmos e Logica de Programação
print("Nicole Carolina Sanches - RA: 0220482523004")

# Calculadora de Investimento com Rentabilidade Condicional
p = float(input("Informe o valor inicial do investimento: "))
t = int(input("Informe o valor do tempo do investimento (em meses):"))

if t < 6:
    tx = 0.005
elif t >= 6 and t <=12:
    tx = 0.008
elif t > 12:
    tx = 0.012

Rendimento_Total = p * tx * t
print(f"A taxa de juros aplocadea  é de {tx} e o rendimento total é de {Rendimento_Total}")