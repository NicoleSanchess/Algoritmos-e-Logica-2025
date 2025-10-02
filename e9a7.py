# Exercício: Verificador de Elegibilidade para Desconto em Streaming

tp = input("Importe o tipo de plano  (digite 'premium', 'padrão' ou 'básico'):")
ta = int(input("Informe o tempo de assinatura (em meses, número inteiro):"))
cc = input("Informe se a conta é compartilhada (digite 'sim' ou 'não'):")

if tp =="premium" and ta >=24:
    print("Você é um cliente premium de longa data: 25% de desconto vitalício!")
elif tp == "padrão" and ta >12 and cc=="não":
    print("Você atende aos critérios para um desconto de 15%.")
elif tp == "basico" and ta >6:
    print( "Sua lealdade merece um reconhecimento: 5% de desconto na próxima fatura.")
else:
    print( "Nenhum desconto disponível no momento para o seu perfil.")
