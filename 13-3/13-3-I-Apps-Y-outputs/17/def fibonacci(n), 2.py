
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def cube(x):
    return x**3

def get_fibonacci_cubes(n):
    fibonacci_numbers = []
    for i in range(n):
        fibonacci_numbers.append(fibonacci(i))
    return list(map(cube, fibonacci_numbers))

n = int(input())
print(get_fibonacci_cubes(n))

