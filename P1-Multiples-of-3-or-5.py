suma_multiplos_de_cinco_y_tres=0 

for i in range(1, 1000):
    if i % 3==0 or i % 5 ==0:   # Si el residuo de la división de i entre 3 o 5 es 0
        suma_multiplos_de_cinco_y_tres += i # Sumar i a la variable suma_multiplos_de_cinco_y_tres
print(suma_multiplos_de_cinco_y_tres)
