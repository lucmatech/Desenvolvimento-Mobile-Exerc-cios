num = int(input("Digite um valor: "))

if num >= 0:
    for i in range(num + 1):
        print(i, end=", ")
    print("FIM!")
else:
    print("Por favor, digite um número inteiro positivo.")
