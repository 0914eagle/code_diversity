
import math

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    divisors.sort()
    return divisors

def count_divisors(n):
    return len(get_divisors(n))

def main():
    n = int(input())
    print(count_divisors(n))

if __name__ == '__main__':
    main()

