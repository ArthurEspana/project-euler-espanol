def verificar_divisibilidad(num):
    for divisor in range(1, 21):
        if num % divisor != 0:
            return False
    return True

def verificar_condicion():
    num = 1
    while True:
        if verificar_divisibilidad(num):
            return num
        num += 1

def main():
    resultado = verificar_condicion()
    print(resultado)
main()

