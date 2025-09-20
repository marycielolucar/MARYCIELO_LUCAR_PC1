def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

suma_primos = sum(n for n in range(100) if es_primo(n))
print("Suma primos menores que 100:", suma_primos)