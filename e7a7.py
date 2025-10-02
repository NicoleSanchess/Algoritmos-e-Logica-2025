# Exercício: Sistema de Avaliação de Desempenho de Vendas

vv = int(input("Informe o numero de vendas (número inteiro, em R$):"))
tx = float(input("Informe a satisfação do cliente  (em uma escala de 0.0 a 1.0, número decimal):"))
mn = input("Informe se sua meta de clientes foi atingida (digite 'sim' ou 'não'):")

if vv >=50000 and tx >=0.9:
    print("Vendedor de alta performance: classificado como Sênior.")
elif vv >= 30000 and mn == "sim":
    print( "Vendedor de bom desempenho: classificado como Pleno.")
elif tx >= 0.8 or mn == "sim":
    print("Vendedor em desenvolvimento: classificado como Júnior.")
else:
    print("Vendedor em revisão de desempenho: não atende aos critérios mínimos.")