def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)

for n in range(1, 21):
    print(n, ":", fib(n))