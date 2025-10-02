# Exercício: Sistema de Classificação de Candidatos a Vaga de Vendas

ev = int(input("Informe sua experiência (em anos):"))
hc = int(input("Informe sua habilidade de comunicação (em uma escala de 1 a 10, número inteiro):"))
dh = input("Informe a sua disponibilidade de horário (digite 'integral' ou 'meio-período'):")

if ev >2 and hc >8:
    print( "Candidato classificado como Sênior. Entra na próxima etapa para vaga integral.")
elif ev >2 and hc >6:
    print("Candidato classificado como Sênior. Entra na próxima etapa para vaga de meio período.")
elif ev > 1 and hc >8 and dh == "meio-periodo":
    print( "Candidato classificado como Pleno. Entra na próxima etapa para vaga de meio período.")
elif ev > 1 and hc > 8 and dh == "integral":
    print( "Candidato classificado como Pleno. Entra na próxima etapa para vaga integral.")
elif hc >7 and dh == "meio-periodo":
    print("Candidato classificado como Júnior. Entra na próxima etapa para vaga de meio período.")
elif hc > 7 and dh == "integral":
    print( "Candidato classificado como Júnior. Entra na próxima etapa para vaga integral.")
else:
    print( "Candidato não classificado. Não atende aos requisitos mínimos.")
