def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

numero_evaluar=10
print("Factorial de ", numero_evaluar, " :", factorial(numero_evaluar))