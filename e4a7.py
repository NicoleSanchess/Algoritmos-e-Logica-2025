#Exercício: Sistema de Avaliação de Pedidos de Compras Online

vc = float(input("Informe o valor da compra: "))
sc = input("Informe o status do cliente (digite 'novo' ou 'fiel'):")
tp = input("Informe o tipo de produto (digite 'eletrônico' ou 'livro'):")

if  vc >=200 and sc == "fiel":
    print("Parabéns! Você tem direito a frete grátis e um brinde especial.")
elif vc >=200 or tp == "livro":
    print ( "Você tem direito a frete grátis. Aproveite!")
elif sc == "fiel" and tp =="eletrônico":
    print( "Você tem direito a um desconto de 5% no frete.")
else:
    print("Não há promoções aplicáveis a este pedido.")


