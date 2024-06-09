
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def cube(x):
    return x**3

def solve(n):
    fib_list = []
    for i in range(n):
        fib_list.append(fibonacci(i))
    return list(map(cube, fib_list))

