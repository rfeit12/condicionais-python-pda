# 4.1 Os alunos do PdA estão sendo avaliados, para passar para o próximo ciclo, deverão  tirar 7 na média.
    # Se o aluno tiver nota 6 e for participativo, irá para recuperação.
    # -Senão, será reprovado.
    # Faça um algoritmo que auxilie a avaliar a nota dos alunos.


media_aluno = 6
participativo = True

if media_aluno >= 7:
    print("Aprovado")
elif media_aluno == 6 and participativo == True:
    print("Em recuperação")
else:
    print("Reprovado")
