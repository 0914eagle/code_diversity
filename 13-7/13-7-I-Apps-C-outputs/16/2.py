
def pythagorean_triples_modulo(n):
    count = 0
    for a in range(1, n):
        for b in range(a, n):
            c = (a**2 + b**2) % n
            if a**2 + b**2 == c**2:
                count += 1
    return count

def main():
    n = int(input())
    print(pythagorean_triples_modulo(n))

if __name__ == '__main__':
    main()

