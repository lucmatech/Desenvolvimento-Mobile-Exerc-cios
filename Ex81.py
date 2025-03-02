idades = []

for i in range(8):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    idades.append(idade)

media_idade = sum(idades) / len(idades)

posicoes_acima_25 = [i for i, idade in enumerate(idades) if idade > 25]

maior_idade = max(idades)
posicoes_maior_idade = [i for i, idade in enumerate(idades) if idade == maior_idade]

print("\n===== RESULTADOS =====")
print(f"Média de idade: {media_idade:.2f} anos")
print(f"Posições das pessoas com mais de 25 anos: {posicoes_acima_25 if posicoes_acima_25 else 'Nenhuma'}")
print(f"Maior idade digitada: {maior_idade} anos")
print(f"Posições da maior idade: {posicoes_maior_idade}")
