def Gerador(mensagem):
    tamanho = len(mensagem) + 4
    print("+" + "=" * tamanho + "+")
    print(f"| {mensagem} |")
    print("+" + "=" * tamanho + "+")

Gerador("Aprendendo Python")
Gerador("Criando um gerador de mensagens")
Gerador("Python é incrível!")
