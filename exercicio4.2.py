# 4.2 A PDA quer verificar se o Tiago está qualificado tirar férias. Para estar em condições, os seguintes requisitos devem ser satisfeito:
    # - Ter trabalhado no mínimo 12 meses completos.
    # - Ter disponibilidade de tirar férias entre dezembro e janeiro.
    # Faca um algoritmo que valide ou não essas duas opções para saber se o Tiago pode tirar férias. O programa deverá escrever a mensagem “Tiago pode sair de férias “ ou  “Tiago não pode sair de férias”.



meses_trabalhados =  12
disponibilidade_ferias = ["Janeiro", "Julho", "Dezembro"]

if meses_trabalhados >= 12 and "Janeiro" and "Dezembro" in disponibilidade_ferias:
    print("Tiago pode sair de férias")
else:
    print("Tiago não pode sair de férias")
