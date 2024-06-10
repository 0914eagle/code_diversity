
def get_pythagorean_triples_modulo(n):
    count = 0
    for a in range(1, n):
        for b in range(a, n):
            c = int((a**2 + b**2)**0.5)
            if a**2 + b**2 == c**2 and a <= b and a <= c and b <= c:
                count += 1
    return count

def main():
    n = int(input())
    print(get_pythagorean_triples_modulo(n))

if __name__ == '__main__':
    main()

