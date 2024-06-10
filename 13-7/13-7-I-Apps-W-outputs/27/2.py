
def get_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def get_ways(n, k, S, a):
    ways = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if a[i] + a[j] == S:
                ways += 1
    return ways

def main():
    n, k, S = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_ways(n, k, S, a))

if __name__ == '__main__':
    main()

