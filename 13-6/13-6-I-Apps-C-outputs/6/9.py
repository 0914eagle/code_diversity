
def f(b, n):
    if n < b:
        return n
    else:
        return f(b, int(n / b)) + (n % b)

def find_b(n, s):
    for b in range(2, 1000000000000):
        if f(b, n) == s:
            return b
    return -1

if __name__ == '__main__':
    n, s = map(int, input().split())
    print(find_b(n, s))

