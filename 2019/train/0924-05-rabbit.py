def rabbit_aka_fibonacci(n):
    return 1 if n == 1 or n == 2 else rabbit_aka_fibonacci(n - 1) + rabbit_aka_fibonacci(n - 2)


def rabbit_aka_fibonacci_2(n):
    a = 0
    b = 1
    count = 0
    while count < n - 1:
        a, b = b, a + b
        count += 1
    return b


print(rabbit_aka_fibonacci(20))
