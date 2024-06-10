
import math

def is_triangle(a, b, c):
    return a**2 + b**2 == c**2

def is_pythagorean_triple(a, b, c):
    return a <= b and is_triangle(a, b, c)

def count_pythagorean_triples(n):
    count = 0
    for a in range(1, n):
        for b in range(a, n):
            c = math.sqrt(a**2 + b**2)
            if c == int(c) and is_pythagorean_triple(a, b, int(c)):
                count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    print(count_pythagorean_triples(n))

