
def input_data():
    n = int(input())
    return n

def pythagorean_triples_modulo_n(n):
    count = 0
    for a in range(1, n):
        for b in range(a, n):
            c = int((a**2 + b**2) % n)
            if a <= b and a**2 + b**2 == c**2:
                count += 1
    return count

def main():
    n = input_data()
    print(pythagorean_triples_modulo_n(n))

if __name__ == '__main__':
    main()

