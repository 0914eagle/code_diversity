
def get_period(s):
    k = 1
    while k < len(s):
        if s[:k] * int(len(s) / k) == s:
            return k
        k += 1
    return 1

def count_distinct_periods(a, b):
    count = 0
    for i in range(1, a + b + 1):
        for j in range(1, a + b + 1):
            s = "A" * i + "B" * j
            count += 1
    return count

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(count_distinct_periods(a, b))

