
def get_k_rounding(n, k):
    if n == 0:
        return 0
    x = 1
    while x < n:
        x *= 10
    while x % n != 0:
        x //= 10
    if x % 10 ** k == 0:
        return x
    else:
        return x * 10

def main():
    n, k = map(int, input().split())
    print(get_k_rounding(n, k))

if __name__ == '__main__':
    main()

