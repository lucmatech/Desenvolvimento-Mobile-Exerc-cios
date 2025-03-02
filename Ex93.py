def Contador(inicio, fim, incremento):
    """Realiza uma contagem com os parâmetros informados."""
    if incremento == 0:
        incremento = 1

    if inicio > fim and incremento > 0:
        incremento = -incremento

    for i in range(inicio, fim, incremento):
        print(i, end=" >> ")

    print("FIM")

ini = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))
inc = int(input("Digite o valor do incremento: "))

Contador(ini, fim, inc)
