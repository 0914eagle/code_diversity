
def get_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def get_ways(n, k, s, cubes):
    ways = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if get_factorial(cubes[i]) + get_factorial(cubes[j]) == s:
                ways += 1
    return ways

def main():
    n, k, s = map(int, input().split())
    cubes = list(map(int, input().split()))
    print(get_ways(n, k, s, cubes))

if __name__ == '__main__':
    main()

