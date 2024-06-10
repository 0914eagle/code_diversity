
def is_pythagorean_triple(a, b, c):
    return a**2 + b**2 == c**2

def count_pythagorean_triples(n):
    count = 0
    for a in range(1, n):
        for b in range(a, n):
            c = (a**2 + b**2) % n
            if is_pythagorean_triple(a, b, c):
                count += 1
    return count

def main():
    n = int(input())
    print(count_pythagorean_triples(n))

if __name__ == '__main__':
    main()

