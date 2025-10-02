# Nicole Carolina Sanches
# RA: 0220482523004
# Avaliação Algoritmos e Logica de Programação
print("Nicole Carolina Sanches - RA: 0220482523004")

# Calculadora de Nível de Glicose
vg = float(input("Informe o valor da glicose: "))

if vg <100:
    print("Glicemia Normal.")
elif vg >=100 and vg <=125:
    print( "Pré-diabetes: Risco Moderado.")
elif vg >125:
    print( "Diabetes: Nível Alto.")