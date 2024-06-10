
def get_pythagorean_triples(n):
    count = 0
    for a in range(1, n):
        for b in range(a, n):
            c = int(math.sqrt(a**2 + b**2))
            if a**2 + b**2 == c**2 and a <= b:
                count += 1
    return count

def get_pythagorean_triples_modulo(n):
    count = 0
    for a in range(1, n):
        for b in range(a, n):
            c = int(math.sqrt(a**2 + b**2))
            if a**2 + b**2 == c**2 and a <= b and (a*b*c) % n == 0:
                count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    print(get_pythagorean_triples_modulo(n))

