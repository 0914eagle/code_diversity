
def get_period(s):
    for i in range(1, len(s)):
        if len(s) % i != 0:
            continue
        if all(s[i * j] == s[j] for j in range(i)):
            return i
    return len(s)

def get_different_periods(a, b):
    s = "A" * a + "B" * b
    return len(set(get_period(s[i:i+j]) for i in range(len(s)) for j in range(1, len(s) - i + 1)))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(get_different_periods(a, b))

