def hallar_primos(num):
    factores = []   # Abro lista
    i = 2  # Empiezo a buscar factores desde el 2
    while i * i <= num: # Mientras el cuadrado del factor sea menor o igual al número
        while num % i == 0: # Mientras el número sea divisible por el factor
            factores.append(i)  # Agregar el factor a la lista
            num = num // i  # Dividir el número por el factor
        i += 1
    if num > 1:  # Si el número restante es mayor que 1, también es un factor primo
        factores.append(num)
    return factores 

def main():
    num = 600851475143
    factores_primos = hallar_primos(num)
    print(max(factores_primos))

main()


# Aprendí append y como funciona exactamente el return, tambien que se puede definir la función directamente en el main