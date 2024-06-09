
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def cube(x):
    return x**3

def solve(n):
    fib_list = [fibonacci(i) for i in range(n)]
    return list(map(cube, fib_list))

