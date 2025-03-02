notas = []

for i in range(10):
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    notas.append(nota)

media_turma = sum(notas) / len(notas)

acima_da_media = [nota for nota in notas if nota > media_turma]
quantidade_acima_media = len(acima_da_media)

maior_nota = max(notas)
posicoes_maior_nota = [i for i, nota in enumerate(notas) if nota == maior_nota]

print("\n===== RESULTADOS =====")
print(f"Média da turma: {media_turma:.2f}")
print(f"Quantidade de alunos acima da média: {quantidade_acima_media}")
print(f"Maior nota digitada: {maior_nota}")
print(f"Posições da maior nota: {posicoes_maior_nota}")
