def SuperSomador(a, b):
    """Retorna a soma de todos os números no intervalo entre a e b, incluindo ambos."""
    if a > b:
        a, b = b, a

    soma = sum(range(a, b + 1))
    return soma

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = SuperSomador(num1, num2)
print(f"A soma dos números entre {num1} e {num2} é {resultado}.")
