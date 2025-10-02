distancia = float(input("Informe a distancia: "))
velocidade = float(input("Informe a velocidade: "))

tempo = distancia / velocidade

if tempo > 4:
    print("Viagem demorada, utilizar veículo sedan")

else:
    print("Viagem rápida, utilizar veículo hatch")