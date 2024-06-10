
import itertools

def is_pythagorean_triple(a, b, c, mod):
    return a**2 + b**2 == c**2 % mod

def count_pythagorean_triples(n):
    count = 0
    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                if is_pythagorean_triple(a, b, c, n):
                    count += 1
    return count

def main():
    n = int(input())
    print(count_pythagorean_triples(n))

if __name__ == '__main__':
    main()

