def Potencia(base, expoente):
    """Calcula a potência de base elevada ao expoente."""
    return base ** expoente

base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = Potencia(base, expoente)
print(f"{base}^{expoente} = {resultado}")
