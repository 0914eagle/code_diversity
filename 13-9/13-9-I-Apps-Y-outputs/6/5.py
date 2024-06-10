
def get_input():
    return list(map(int, input().split()))

def get_flavor_sum(apples, apple_to_eat):
    return sum(apples[apple_to_eat+1:])

def get_min_diff(apples):
    min_diff = float('inf')
    for apple_to_eat in range(len(apples)):
        flavor_sum = get_flavor_sum(apples, apple_to_eat)
        diff = abs(flavor_sum - sum(apples))
        if diff < min_diff:
            min_diff = diff
            optimal_apple_to_eat = apple_to_eat
    return min_diff, optimal_apple_to_eat

def main():
    N, L = get_input()
    apples = [L+i-1 for i in range(1, N+1)]
    min_diff, optimal_apple_to_eat = get_min_diff(apples)
    print(get_flavor_sum(apples, optimal_apple_to_eat))

if __name__ == '__main__':
    main()

