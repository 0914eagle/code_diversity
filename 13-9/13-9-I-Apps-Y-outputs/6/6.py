
def get_input():
    return list(map(int, input().split()))

def get_apple_pie_flavor(apples, apple_to_eat):
    return sum(apples) - apples[apple_to_eat]

def get_optimal_apple_to_eat(apples):
    optimal_apple_to_eat = 0
    optimal_flavor_diff = float('inf')
    for apple_to_eat in range(len(apples)):
        flavor_diff = abs(get_apple_pie_flavor(apples, apple_to_eat) - sum(apples))
        if flavor_diff < optimal_flavor_diff:
            optimal_flavor_diff = flavor_diff
            optimal_apple_to_eat = apple_to_eat
    return optimal_apple_to_eat

def main():
    n, l = get_input()
    apples = list(range(l, l + n))
    optimal_apple_to_eat = get_optimal_apple_to_eat(apples)
    print(get_apple_pie_flavor(apples, optimal_apple_to_eat))

if __name__ == '__main__':
    main()

