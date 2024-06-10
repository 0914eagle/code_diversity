
def read_input():
    return list(map(int, input().split()))

def get_flavor(apples, apple_to_eat):
    return sum(apples) - apples[apple_to_eat]

def get_optimal_flavor(apples):
    n = len(apples)
    optimal_flavor = 0
    for apple_to_eat in range(n):
        flavor = get_flavor(apples, apple_to_eat)
        if flavor < optimal_flavor or optimal_flavor == 0:
            optimal_flavor = flavor
    return optimal_flavor

def main():
    n, l = read_input()
    apples = [l + i for i in range(n)]
    print(get_optimal_flavor(apples))

if __name__ == '__main__':
    main()

