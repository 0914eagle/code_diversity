
def get_flavor(apples, apple_to_eat):
    return sum(apples) - apples[apple_to_eat]

def get_optimal_flavor(apples):
    n = len(apples)
    if n == 1:
        return apples[0]
    if n == 2:
        return apples[0] + apples[1]
    optimal_flavor = 0
    for i in range(n):
        flavor = get_flavor(apples, i)
        if flavor < optimal_flavor or optimal_flavor == 0:
            optimal_flavor = flavor
    return optimal_flavor

if __name__ == '__main__':
    n, l = map(int, input().split())
    apples = [int(input()) for _ in range(n)]
    print(get_optimal_flavor(apples))

