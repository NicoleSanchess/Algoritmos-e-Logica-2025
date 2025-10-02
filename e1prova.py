# Nicole Carolina Sanches
# RA: 0220482523004
# Avaliação Algoritmos e Logica de Programação
print("Nicole Carolina Sanches - RA: 0220482523004")

# Classificador de Lucro de Vendas
pc = float(input("Informe o preço de custo do produto: "))
pv = float(input("Informe o preço de venda do produto: "))

lucro = pv - pc
margem = (lucro / pc) * 100

if margem > 30:
    print( "Margem Excelente!")
elif margem >= 10  and margem <=30:
    print( "Margem Satisfatória.")
elif margem < 10:
    print("Margem Baixa: Avaliar preço de venda.")
