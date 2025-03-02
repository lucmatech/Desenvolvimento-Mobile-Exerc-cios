import random

opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Escolha pedra, papel ou tesoura: ").strip().lower()

computador = random.choice(opcoes)

print(f"\nVocê escolheu: {jogador}")
print(f"O computador escolheu: {computador}")

if jogador == computador:
    resultado = "EMPATE!"
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    resultado = "VOCÊ VENCEU!"
elif jogador in opcoes:
    resultado = "O COMPUTADOR VENCEU!"
else:
    resultado = "Jogada inválida! Escolha pedra, papel ou tesoura."

print(resultado)
