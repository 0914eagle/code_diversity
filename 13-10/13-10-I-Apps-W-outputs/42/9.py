
def get_period(s):
    k = 1
    while k < len(s):
        if s[:k] * (len(s) // k) == s:
            return k
        k += 1
    return len(s)

def count_periods(a, b):
    count = 0
    for i in range(a):
        for j in range(b):
            s = "A" * i + "B" * j
            count += 1
    return count

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(count_periods(a, b))

