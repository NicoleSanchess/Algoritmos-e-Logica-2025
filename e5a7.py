# Exercício: Avaliação de Candidato para Bolsa de Estudos

ma = float(input("Informe sua média acadêmica: "))
he = int(input("Infurme sua habilidade acadêmica  (em uma escala de 1 a 5, número inteiro):"))
s = input("Informe se há necessidade finaceira  (digite 'sim' ou 'não'):")

if ma >=9 and he>=4:
    print( "Parabéns! Você é elegível para a bolsa de mérito acadêmico.")
elif ma >=8 and s == "sim":
    print("Parabéns! Você é elegível para a bolsa de necessidade financeira.")
elif ma >=7 and he>=3 and s == "sim":
    print( "Parabéns! Você é elegível para a bolsa combinada de mérito e necessidade.")
elif ma >=7 and he>=3:
    print( "Você é elegível para a bolsa de necessidade, mas sua média e habilidade em escrita são requisitos.")
else:
    print( "Infelizmente, você não atende aos critérios de elegibilidade para bolsa.")