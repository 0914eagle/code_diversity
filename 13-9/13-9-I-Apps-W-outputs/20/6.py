
def k_rounding(n, k):
    # Find the smallest number that ends with k or more zeros and is divisible by n
    x = n
    while x % 10 != 0 or len(str(x)) <= k:
        x *= 10
    return x

def main():
    n, k = map(int, input().split())
    print(k_rounding(n, k))

if __name__ == '__main__':
    main()

