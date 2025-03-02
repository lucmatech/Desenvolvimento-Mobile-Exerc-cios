nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media <= 4.9:
    situacao = "REPROVADO"
elif 5.0 <= media <= 6.9:
    situacao = "RECUPERAÇÃO"
else:
    situacao = "APROVADO"

print(f"A média do aluno foi {media:.1f}. Situação: {situacao}.")