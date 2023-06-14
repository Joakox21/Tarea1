def es_primo(numero):
    if numero < 2:
        return False  # Los números menores a 2 no son primos

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False  # Se encontró un divisor, por lo tanto no es primo

    return True  # No se encontraron divisores, es primo