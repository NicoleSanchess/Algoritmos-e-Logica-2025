# Exercício: Classificador de Acesso a Evento

ti = input("Informe o tipo do ingresso (digite 'padrão' ou 'premium'):")
idade = int(input("Informe a sua idade:"))
vip = input("Lista de convidados VIP? (digite 'sim' ou 'não'):")

if  ti == "premium":
    print( "Acesso total: todas as áreas e benefícios especiais.")
elif idade>=18 and vip == "sim":
    print("Acesso VIP: área exclusiva e entrada prioritária.")
elif idade>=18 or ti == "padrão":
    print( "Acesso padrão: entrada para a área principal do evento.")
else:
    print("Acesso negado: verifique os critérios de entrada.")