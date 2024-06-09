
def gcd(a, b, c):
    return __gcd(a, __gcd(b, c))

def solve(K):
    sum = 0
    for a in range(1, K+1):
        for b in range(1, K+1):
            for c in range(1, K+1):
                sum += gcd(a, b, c)
    return sum

def main():
    K = int(input())
    print(solve(K))

if __name__ == '__main__':
    main()

