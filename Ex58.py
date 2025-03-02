soma_idades = 0
quantidade_alunos = 0

print("Digite a idade dos alunos (Digite 999 para encerrar)")

while True:
    idade = int(input("Digite a idade do aluno: "))

    if idade == 999:  
        break

    soma_idades += idade
    quantidade_alunos += 1

if quantidade_alunos > 0:
    media_idade = soma_idades / quantidade_alunos
else:
    media_idade = 0

print("\n===== RESULTADOS =====")
print(f"Total de alunos cadastrados: {quantidade_alunos}")
print(f"Média de idade do grupo: {media_idade:.2f} anos")
