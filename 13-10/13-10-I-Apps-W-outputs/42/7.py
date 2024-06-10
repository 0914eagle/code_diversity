
def get_period(s):
    k = 1
    while k < len(s):
        if s[:k] * (len(s) // k) == s:
            return k
        k += 1
    return 1

def count_periods(a, b):
    periods = set()
    for i in range(a+b):
        s = "A" * i + "B" * (a+b-i)
        periods.add(get_period(s))
    return len(periods)

def main():
    a, b = map(int, input().split())
    print(count_periods(a, b))

if __name__ == '__main__':
    main()

