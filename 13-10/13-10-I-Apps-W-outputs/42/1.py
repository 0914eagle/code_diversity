
def get_period(s):
    k = 1
    while k < len(s):
        if s[:k] * (len(s) // k) == s:
            return k
        k += 1
    return len(s)

def get_all_periods(a, b):
    periods = set()
    for i in range(a):
        for j in range(b):
            s = 'A' * i + 'B' * j
            periods.add(get_period(s))
    return periods

def get_number_of_periods(a, b):
    return len(get_all_periods(a, b))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(get_number_of_periods(a, b))

