horas = float(input("Quantas horas de atividade física você fez neste mês? "))

if horas <= 10:
    pontos = horas * 2
elif horas <= 20:
    pontos = (10 * 2) + ((horas - 10) * 5)
else:
    pontos = (10 * 2) + (10 * 5) + ((horas - 20) * 10)

dinheiro = pontos * 0.05

print(f"\nVocê acumulou {pontos:.0f} pontos.")
print(f"Valor ganho: R$ {dinheiro:.2f}")
