
def get_max_candies(n, k, M, D):
    max_candies = 0
    for x in range(1, M+1):
        if n % x == 0 and n // x <= k:
            max_candies = max(max_candies, n // x)
    return max_candies

def main():
    n, k, M, D = map(int, input().split())
    print(get_max_candies(n, k, M, D))

if __name__ == '__main__':
    main()

