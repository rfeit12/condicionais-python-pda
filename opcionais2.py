# DESAFIOS EXTRAS - OPCIONAIS
# DESAFIO_02 = Precisamos identificar a menor média de um aluno para saber se ele pode seguir para a próxima fase de um projeto.

# Faça um programa que peça as três notas do aluno e imprima a menor deles.

nota1 = input("Digite a primeira nota:")
nota2 = input("Digite a segunda nota:")
nota3 = input("Digite a terceira nota:")

if nota1 < nota2 and nota3:
    print("Sua menor nota é: " + nota1)
elif nota2 < nota1 and nota3:
    print("Sua menor nota é: " + nota2)
else:
    print("Sua menor nota é: " + nota3)