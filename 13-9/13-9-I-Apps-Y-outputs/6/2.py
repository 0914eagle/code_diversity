
def get_input():
    return list(map(int, input().split()))

def get_apple_pie_flavor(apples, n):
    return sum(apples[:n])

def get_optimal_apple_to_eat(apples, n):
    optimal_apple_to_eat = 0
    min_diff = float('inf')
    for i in range(n):
        diff = abs(get_apple_pie_flavor(apples, n) - get_apple_pie_flavor(apples, n-1))
        if diff < min_diff:
            min_diff = diff
            optimal_apple_to_eat = i
    return optimal_apple_to_eat

def main():
    n, L = get_input()
    apples = [L+i-1 for i in range(1, n+1)]
    optimal_apple_to_eat = get_optimal_apple_to_eat(apples, n)
    print(optimal_apple_to_eat)

if __name__ == '__main__':
    main()

