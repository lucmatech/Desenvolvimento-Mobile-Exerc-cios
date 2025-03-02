peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    classificacao = "Peso ideal"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
elif 30 <= imc < 40:
    classificacao = "Obesidade"
else:
    classificacao = "Obesidade mórbida"

print(f"\nSeu IMC é {imc:.1f}. Classificação: {classificacao}.")
