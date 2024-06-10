
def get_pythagorean_triples_modulo(n):
    count = 0
    for a in range(1, n):
        for b in range(a, n):
            c = (a**2 + b**2) % n
            if a <= b and c > 0 and (a*a + b*b) % n == c*c:
                count += 1
    return count

def main():
    n = int(input())
    print(get_pythagorean_triples_modulo(n))

if __name__ == '__main__':
    main()

