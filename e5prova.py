# Nicole Carolina Sanches
# RA: 0220482523004
# Avaliação Algoritmos e Logica de Programação
print("Nicole Carolina Sanches - RA: 0220482523004")

# Cálculo de Custo Final de Produção com Penalidade
C_inicial = float(input("Informe o custo inicial do material:"))
Q = int(input("Informe a quantidade de itens produzidos: "))
Dias = int(input("Informe o numero de dias de atraso: "))
PD = float(input("Informe o percentual de defeitos (Defeito, em decimal, ex: 0.05 para 5%): "))

if Q >1000 and C_inicial > 5000:
    F_comp = 1.15
else:
    F_comp = 1.05

C_corrigido = C_inicial * F_comp
if PD > 0.10 or Dias > 5:
    C_final = C_corrigido * 1.25
    print(f"Penalidade Alta: 20% de redução no lucro. Seu custo base corrigido foi de {C_corrigido} e o custo final do lote é de {C_final}")
elif PD >= 0.05 and PD <= 0.10 and Dias > 0:
    C_final = C_corrigido * 1.10
    print(f"Penalidade Média: 10% de redução no lucro. Seu custo base corrigido foi de {C_corrigido} e o custo final do lote é de {C_final}")
else:
    C_final = C_corrigido
    print (f"Sem penalidade. Custo final apenas com correção. Seu custo base corrigido foi de {C_corrigido} e o custo final do lote é de {C_final}")

