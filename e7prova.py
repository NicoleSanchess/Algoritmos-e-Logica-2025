# Nicole Carolina Sanches
# RA: 0220482523004
# Avaliação Algoritmos e Logica de Programação
print("Nicole Carolina Sanches - RA: 0220482523004")

# Exercício: Classificador de Lote Químico e Preço Variável
pureza = float(input("Informe a pureza do lote (em porcentagem, ex: 0.95 para 95%): "))
massa = float(input("Informe o valor da massa (em kg): "))
taxa_contaminacao = float(input("Informe a taxa de contaminação (em porcentagem, ex: 0.02 para 2%):"))

FD = (pureza * 100) - (taxa_contaminacao * 50)
if massa > 1000:
    P_base = 10.00
else:
    P_base = 12.50

if FD > 90 and pureza > 0.98:
    P_final_kg = P_base * 1.50
    print( "Classificação: PREMIUM (Venda Imediata)")
elif FD >= 70 and FD <= 90 and taxa_contaminacao < 0.05:
    P_final_kg = P_base * 1.10
    print ("Classificação: PADRÃO (Venda Normal)")
elif FD < 70 or pureza < 0.90:
    P_final_kg = P_base * 0.25 
    print( "Classificação: REPROVADO (Descarte ou Re-processamento)")
else:
    P_final_kg = P_base * 0.90
    print("Classificação: ACEITÁVEL (Margem Mínima)")

Preco_Total_Final = P_final_kg * massa
print(f"O preço base por kg  é de {P_base} e o preço final total é de {Preco_Total_Final}")

