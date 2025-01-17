# Definimos la variable primer y segundo con valor 1 porque la serie de fibonacci empieza con 1 y 1 luego estas variables se iran actualizando con los valores de la serie de fibonacci
primer = 1
segundo = 1
valores_pares_fibonacci = 0 

while segundo < 4000000:
    if segundo % 2 == 0: # Si el residuo de la división de segundo entre 2 es 0
        valores_pares_fibonacci += segundo # Sumar segundo a la variable valores_pares_fibonacci porque es un número par
    next_fib = primer + segundo    # Respetamos la secuencia de fibonacci
    primer = segundo # Actualizamos el valor de primer con el valor de segundo, lo utilizaremos en la siguiente iteración
    segundo = next_fib # Actualizamos el valor de segundo con el valor de next_fib, lo utilizaremos en la siguiente iteración

print(valores_pares_fibonacci)
