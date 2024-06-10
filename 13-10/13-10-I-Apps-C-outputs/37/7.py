
import math

def is_pythagorean_triplet(a, b, c, n):
    if a <= b:
        if a**2 + b**2 == c**2:
            if a >= 1 and b >= 1 and c >= 1:
                if a < n and b < n and c < n:
                    return True
    return False

def count_pythagorean_triplets(n):
    count = 0
    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                if is_pythagorean_triplet(a, b, c, n):
                    count += 1
    return count

def main():
    n = int(input())
    print(count_pythagorean_triplets(n))

if __name__ == '__main__':
    main()

