a = float(input("Digite o comprimento do primeiro segmento: "))
b = float(input("Digite o comprimento do segundo segmento: "))
c = float(input("Digite o comprimento do terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("Os segmentos podem formar um TRIÂNGULO!")
else:
    print("Os segmentos NÃO podem formar um triângulo.")
