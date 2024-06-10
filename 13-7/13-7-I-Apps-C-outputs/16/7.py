
def is_pythagorean_triple(a, b, c):
    return a**2 + b**2 == c**2

def count_pythagorean_triples(n):
    count = 0
    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                if is_pythagorean_triple(a, b, c) and a <= b:
                    count += 1
    return count

def count_pythagorean_triples_modulo(n):
    count = 0
    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                if is_pythagorean_triple(a, b, c) and a <= b and c**2 % n == (a**2 + b**2) % n:
                    count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    print(count_pythagorean_triples_modulo(n))

