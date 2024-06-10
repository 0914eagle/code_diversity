
def get_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if n // i != i:
                factors.append(n // i)
    return sorted(factors)

def get_ways(n, k, S):
    ways = 0
    for i in range(1, n+1):
        factors = get_factors(i)
        for factor in factors:
            if factor <= k:
                ways += 1
    return ways

def main():
    n, k, S = map(int, input().split())
    print(get_ways(n, k, S))

if __name__ == '__main__':
    main()

