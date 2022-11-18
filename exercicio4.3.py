# 4.3 A PdA fará uma confraternização em um grande parque aquático em São Paulo, mas para conseguir se programar e fechar a data precisa analisar a temperatura.
# Faça um programa que avalie e entregue as seguintes respostas:
# - Maior que 25 graus ("Oba! A PDA pode marcar a data").
# - Menor ou igual a 25 graus ("Vamos! O que vale é a companhia").
# - Menor ou igual a 15 graus ("Estará muito frio, não podemos alugar nessa data").



temperatura = 20

if temperatura <= 15:
    print("Estará muito frio, não podemos alugar nessa data")
elif temperatura <= 25:
    print("Vamos! O que vale é a companhia")
else:
    print("Oba! A PDA pode marcar a data")