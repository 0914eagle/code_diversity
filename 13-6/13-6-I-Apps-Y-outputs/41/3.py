
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def sum_gcd(n):
    return sum([gcd(i, j, k) for i in range(1, n+1) for j in range(1, n+1) for k in range(1, n+1)])

def main():
    n = int(input())
    print(sum_gcd(n))

if __name__ == '__main__':
    main()

