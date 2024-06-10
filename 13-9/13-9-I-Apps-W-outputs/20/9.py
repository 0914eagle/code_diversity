
def k_round(n, k):
    # Find the minimum integer x such that x ends with k or more zeros and is divisible by n
    x = n
    while x % 10 != 0 or len(str(x)) <= k:
        x *= 10
    return x

def main():
    n, k = map(int, input().split())
    print(k_round(n, k))

if __name__ == '__main__':
    main()

