soma_alturas = 0
pessoas_acima_90kg = 0
pessoas_abaixo_50kg_160cm = 0
pessoas_acima_190cm_100kg = 0

for i in range(1, 8):
    print(f"\n--- {i}ª PESSOA ---")
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))

    soma_alturas += altura

    if peso > 90:
        pessoas_acima_90kg += 1
    if peso < 50 and altura < 1.60:
        pessoas_abaixo_50kg_160cm += 1
    if altura > 1.90 and peso > 100:
        pessoas_acima_190cm_100kg += 1

media_altura = soma_alturas / 7

print("\n===== RESULTADOS =====")
print(f"Média de altura do grupo: {media_altura:.2f} m")
print(f"Quantidade de pessoas com mais de 90Kg: {pessoas_acima_90kg}")
print(f"Quantidade de pessoas com menos de 50Kg e altura abaixo de 1.60m: {pessoas_abaixo_50kg_160cm}")
print(f"Quantidade de pessoas com mais de 1.90m e peso acima de 100Kg: {pessoas_acima_190cm_100kg}")
