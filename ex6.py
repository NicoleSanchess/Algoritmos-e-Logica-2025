nota1 = float(input("Informe o valor da primeira nota: "))
nota2 = float(input("Informe o valor da segunda nota: "))

media= (nota1+nota2)/2

if media >= 6:
    print(f"Você foi APROVADO, sua média é {media}")

else:
    print(f"Você foi REPROVADO, sua média é {media}")

    