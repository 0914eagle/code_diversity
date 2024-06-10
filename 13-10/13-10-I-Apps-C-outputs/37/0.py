
import math

def triangle_numbers(n):
    triangles = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i**2 + j**2 == (i+j)**2:
                triangles.append((i, j, i+j))
    return triangles

def pythagorean_triples_modulo(n):
    triangles = triangle_numbers(n)
    pythagorean_triples = []
    for triangle in triangles:
        a, b, c = triangle
        if a <= b and a**2 + b**2 == c**2:
            pythagorean_triples.append(triangle)
    return pythagorean_triples

def main():
    n = int(input())
    print(len(pythagorean_triples_modulo(n)))

if __name__ == '__main__':
    main()

