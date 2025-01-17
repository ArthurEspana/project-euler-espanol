# Un palíndromo es cuando el numero se ve de la misma manera de izquierda a derecha y de derecha a izquierda por ejemplo el 9009 es un palíndromo.
# Para hallar el palindromo mas grande de un numero de 3 digitos se puede hacer un ciclo for que recorra los numeros de 100 a 999 y multiplicarlos entre si

def main():
    palindromo = 0
    # El range() genera una secuencia de números que van desde 0 por defecto hasta el número que se pasa como parámetro menos 1. En realidad, se pueden pasar hasta tres parámetros separados por coma, donde el primer es el inicio de la secuencia, el segundo el final y el tercero el salto que se desea entre números. Por defecto se empieza en 0 y el salto es de 1.
    for i in range(100, 1000): # En este caso, el rango va desde el 100 hasta el 999, tomando el salto de 1 en 1
        for j in range(100, 1000):
            producto = i * j
            if str(producto) == str(producto)[::-1] and producto > palindromo_mas_alto: # Convertimos el producto a string y lo comparamos con su reverso si es igual y es mayor al palindromo mas alto encontrado previamente, guarda el valor del numero mas alto
                palindromo_mas_alto = producto
    print(palindromo)

main()