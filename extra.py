import math

a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

delta =  b*b - 4 * a * c

if delta < 0:
    print(f"Delta é negativo ({delta}).")
else:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print(f"O resultado delta é {delta} e as raízes da equação são x1 = {x1} e x2 = {x2}") 