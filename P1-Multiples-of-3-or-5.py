suma_cinco_y_tres=0 

for i in range(1, 1000):
    if i % 3==0 or i % 5 ==0:
        suma_cinco_y_tres += i

print(suma_cinco_y_tres)


# Puse demasiadas variables, y estaba iterando una variable "numero" en vez de i