
import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def period_count(a, b):
    periods = set()
    for i in range(1, a + b + 1):
        period = i
        while period <= a + b:
            if period == i:
                periods.add(i)
            period *= 2
    return len(periods)

def main():
    a, b = map(int, sys.stdin.readline().split())
    print(period_count(a, b))

if __name__ == '__main__':
    main()

