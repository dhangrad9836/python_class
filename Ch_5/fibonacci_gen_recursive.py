def fib_gen1(n):
    fib_n = n
    if n > 1:
        fib_n = fib_gen1(n-2) + fib_gen1(n-1)
    print(fib_n)
    return fib_n

fib_gen1(6)