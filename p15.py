# Compute n-th fibonacci number

def fibonacci(n):
    base = [0,1]
    if n < 2:
        return base[n]

    first = 0
    second = 1
    for x in range(n-1):
        fib = first + second
        first = second
        second = fib

    return fib

print fibonacci(0)
print fibonacci(1)
print fibonacci(2)
print fibonacci(3)
print fibonacci(4)
print fibonacci(5)
