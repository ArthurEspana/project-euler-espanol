first = 1
second = 1
even_fibonacci = 0

while second < 4000000:
    if second % 2 == 0:
        even_fibonacci += second

    next_fib = first + second
    first = second
    second = next_fib

print(even_fibonacci)


# Use for en vez de while y estaba iterando uno a uno, tardaba demasiado