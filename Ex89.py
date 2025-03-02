def Gerador(mensagem, repeticoes, borda_tipo):
    bordas = {
        1: "+-------=======------+",
        2: "~~~~~~~~:::::::~~~~~~~",
        3: "<<<<<<<<------>>>>>>>>"
    }

    borda = bordas.get(borda_tipo, bordas[1])

    print(borda)

    for _ in range(repeticoes):
        print(mensagem)

    print(borda)

Gerador("Portugol Studio", 3, 2)
