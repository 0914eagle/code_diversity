
def gcd(a, b, c):
    return __gcd(a, __gcd(b, c))

def sum_gcd(K):
    result = 0
    for a in range(1, K+1):
        for b in range(1, K+1):
            for c in range(1, K+1):
                result += gcd(a, b, c)
    return result

def main():
    K = int(input())
    print(sum_gcd(K))

if __name__ == '__main__':
    main()

