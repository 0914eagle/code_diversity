
def get_period(s):
    k = 1
    while k < len(s):
        if s[:k] * (len(s) // k) == s:
            return k
        k += 1
    return len(s)

def get_all_periods(a, b):
    periods = set()
    for i in range(a+b):
        s = "A" * i + "B" * (a+b-i)
        periods.add(get_period(s))
    return periods

def main():
    a, b = map(int, input().split())
    print(len(get_all_periods(a, b)))

if __name__ == '__main__':
    main()

