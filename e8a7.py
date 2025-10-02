# Exercício: Classificador de Pedidos de Pizzaria

tam = input("Informe o tamanho da pizza  (digite 'pequena', 'média' ou 'grande'):")
nm = int(input("Informe o numero de sabores: "))
sc = input("Informe o seu status  (digite 'vip' ou 'normal'): ")

if tam == "grande" and nm >2:
    print("Pedido especial: sujeito a taxa extra.")
elif tam == "grande" or sc == "vip":
    print("Pedido prioritário: prepare para entrega rápida.")
elif tam == "média" and nm == 1:
    print("Pedido padrão: processamento normal.")
else:
    print("Pedido de baixo volume: pode ser processado a qualquer momento.")