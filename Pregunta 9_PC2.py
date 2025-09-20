def es_num_perfecto(numero):
    divisores = [i for i in range(1, numero) if numero % i == 0]
    return sum(divisores) == numero

perfectos = [n for n in range(1, 1000) if es_num_perfecto(n)]
print("Números perfectos < 1000:", perfectos)