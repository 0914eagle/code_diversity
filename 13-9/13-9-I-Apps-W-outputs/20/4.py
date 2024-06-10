
def k_rounding(n, k):
    # Find the minimum integer x such that x ends with k or more zeros and is divisible by n
    x = n * 10 ** k
    while x % n != 0:
        x += 1
    return x

def main():
    n, k = map(int, input().split())
    print(k_rounding(n, k))

if __name__ == '__main__':
    main()

