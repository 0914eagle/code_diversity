
import itertools

def get_period(s):
    period = 1
    for i in range(1, len(s)):
        if s[i] != s[i % period]:
            period += 1
    return period

def get_all_periods(a, b):
    periods = set()
    for i in range(a + b):
        for perm in itertools.permutations('A' * a + 'B' * b):
            period = get_period(''.join(perm))
            periods.add(period)
    return periods

def main():
    a, b = map(int, input().split())
    print(len(get_all_periods(a, b)))

if __name__ == '__main__':
    main()

