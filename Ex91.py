def Maior(valor1, valor2):
    """Verifica e exibe qual valor é maior ou se são iguais."""
    if valor1 > valor2:
        print(f"O maior valor é: {valor1}")
    elif valor2 > valor1:
        print(f"O maior valor é: {valor2}")
    else:
        print("Os dois valores são iguais.")

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

Maior(num1, num2)
