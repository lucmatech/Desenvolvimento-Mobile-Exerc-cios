maior_idade = 0
total_homens = 0
soma_idade_homens = 0
quantidade_homens = 0
idade_mulher_mais_jovem = float('inf')

while True:
    print("\n--- CADASTRO DE PESSOA ---")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo [M/F]: ").strip().upper()

    if idade > maior_idade:
        maior_idade = idade

    if sexo == "M":
        total_homens += 1
        soma_idade_homens += idade
        quantidade_homens += 1
    elif sexo == "F":
        if idade < idade_mulher_mais_jovem:
            idade_mulher_mais_jovem = idade
    else:
        print("Sexo inválido! Considere apenas 'M' ou 'F'.")

    continuar = input("Deseja continuar? [S/N]: ").strip().upper()
    if continuar == "N":
        break

if quantidade_homens > 0:
    media_idade_homens = soma_idade_homens / quantidade_homens
else:
    media_idade_homens = 0

print("\n===== RESULTADOS =====")
print(f"Maior idade lida: {maior_idade} anos")
print(f"Total de homens cadastrados: {total_homens}")
if idade_mulher_mais_jovem == float('inf'):
    print("Nenhuma mulher foi cadastrada.")
else:
    print(f"Idade da mulher mais jovem: {idade_mulher_mais_jovem} anos")
print(f"Média de idade dos homens: {media_idade_homens:.2f} anos")
