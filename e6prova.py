# Nicole Carolina Sanches
# RA: 0220482523004
# Avaliação Algoritmos e Logica de Programação
print("Nicole Carolina Sanches - RA: 0220482523004")

# Avaliador de Desempenho de Investimento 
R_investimento = float(input("Informe o valor do retorno do investimento(em decimal, ex: 0.05 para 5%): "))
R_livre = float(input("Informe a taxa livre de risco(em decimal, ex: 0.05 para 5%): "))
Sigma = float(input("Informe o desvio-padrão da volatilidade (em decimal, ex: 0.05 para 5%): "))

if Sigma == 0:
    print("Não é possivel dividir um valor por 0")
else:
    Sharp = (R_investimento - R_livre) / Sigma

Spread = R_investimento - R_livre
if Sharp > 1.5 and Spread > 0.05:
    print(f"Investimento Excelente: Alta performance ajustada ao risco. O valor do Sharp é de {Sharp}")
elif Sharp >= 0.05 and Sharp<= 1.5 or Spread > 0.02:
    print(f"Investimento Bom: Risco e retorno moderados. O valor do Sharp é de {Sharp}")
elif Sharp < 0.5 and R_investimento > 0:
    print(f"Investimento Aceitável: Retorno positivo, mas risco alto para o ganho. O valor do Sharp é de {Sharp}")
else:
    print(f"Investimento Ruim: Não recomendado.")
