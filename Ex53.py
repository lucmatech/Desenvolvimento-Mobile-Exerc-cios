total_homens = 0
total_mulheres = 0
soma_idades = 0
soma_idades_homens = 0
homens_cadastrados = 0
mulheres_mais_20 = 0

for i in range(1, 6):
    print(f"\n--- {i}ª PESSOA ---")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo [M/F]: ").strip().upper()

    soma_idades += idade

    if sexo == "M":
        total_homens += 1
        soma_idades_homens += idade
        homens_cadastrados += 1
    elif sexo == "F":
        total_mulheres += 1
        if idade > 20:
            mulheres_mais_20 += 1
    else:
        print("Entrada inválida. Considere apenas 'M' ou 'F'.")

media_idade_grupo = soma_idades / 5

if homens_cadastrados > 0:
    media_idade_homens = soma_idades_homens / homens_cadastrados
else:
    media_idade_homens = 0

print("\n===== RESULTADOS =====")
print(f"Total de homens cadastrados: {total_homens}")
print(f"Total de mulheres cadastradas: {total_mulheres}")
print(f"Média de idade do grupo: {media_idade_grupo:.1f} anos")
print(f"Média de idade dos homens: {media_idade_homens:.1f} anos")
print(f"Mulheres com mais de 20 anos: {mulheres_mais_20}")
