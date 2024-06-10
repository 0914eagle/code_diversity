
def is_pythagorean_triplet(a, b, c, n):
    return a <= b and a**2 + b**2 == c**2

def count_pythagorean_triplets(n):
    count = 0
    for a in range(1, n):
        for b in range(a, n):
            c = (a**2 + b**2) % n
            if is_pythagorean_triplet(a, b, c, n):
                count += 1
    return count

def main():
    n = int(input())
    print(count_pythagorean_triplets(n))

if __name__ == '__main__':
    main()

