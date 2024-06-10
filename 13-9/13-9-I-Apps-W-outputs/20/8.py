
def k_rounding(n, k):
    if n == 0:
        return 0
    else:
        x = 1
        while x < n:
            x *= 10
        return x // n * n

def main():
    n, k = map(int, input().split())
    print(k_rounding(n, k))

if __name__ == '__main__':
    main()

