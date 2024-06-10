
def smallest_divisor(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n

def final_value(n, k):
    for _ in range(k):
        n += smallest_divisor(n)
    return n

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(final_value(n, k))
