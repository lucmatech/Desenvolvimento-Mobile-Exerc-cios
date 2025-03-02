valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o seu salário mensal: R$ "))
anos = int(input("Em quantos anos deseja pagar? "))

meses = anos * 12  
prestacao = valor_casa / meses  

limite = salario * 0.3

print(f"\nValor da prestação: R$ {prestacao:.2f}")
print(f"Limite máximo permitido: R$ {limite:.2f}")

if prestacao <= limite:
    print("Empréstimo APROVADO!")
else:
    print("Empréstimo NEGADO! O valor da prestação excede 30% do seu salário.")
