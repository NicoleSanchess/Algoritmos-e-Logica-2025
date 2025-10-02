# Nicole Carolina Sanches
# RA: 0220482523004
# Avaliação Algoritmos e Logica de Programação
print("Nicole Carolina Sanches - RA: 0220482523004")

# Cálculo de Custo de Envio com Taxas Variáveis
pe = float(input("Informe o peso da emcomenda (em kg): "))
de = float(input("Informe a distância de entrega (em km): "))

cbt = (pe * 1.5) + (de * 0.25)

if cbt >200:
    cf = cbt * 0.90
elif cbt >=50 and cbt <=200:
    cf = cbt
elif cbt <50:
    cf = cbt + 5.00

print (f"Seu custo base foi de R${cbt} e o custo final foi de {cf}")