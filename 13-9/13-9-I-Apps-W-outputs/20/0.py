
def k_rounding(n, k):
    x = n * 10 ** k
    while x % n != 0:
        x += 1
    return x

def main():
    n, k = map(int, input().split())
    print(k_rounding(n, k))

if __name__ == '__main__':
    main()

