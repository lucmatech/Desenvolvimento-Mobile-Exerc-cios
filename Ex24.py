distancia = float(input("Digite a distância da viagem em Km: "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"O preço da passagem será de R$ {preco:.2f}")
