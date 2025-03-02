def Fibonacci(n):
    """Gera e exibe a sequência de Fibonacci com n termos."""
    if n <= 0:
        print("Quantidade inválida! Insira um número maior que zero.")
        return

    a, b = 1, 1
    print(a, end=" >> ")

    if n == 1:
        print("FIM")
        return

    print(b, end=" >> ")

    for _ in range(n - 2):
        a, b = b, a + b
        print(b, end=" >> ")

    print("FIM")

termos = int(input("Quantos termos da sequência Fibonacci deseja ver? "))

Fibonacci(termos)
