
def get_flavor(apples, apple_to_eat):
    flavor = 0
    for i in range(len(apples)):
        if i != apple_to_eat:
            flavor += apples[i]
    return flavor

n, l = map(int, input().split())
apples = list(map(int, input().split()))

min_diff = 101
optimal_apple = 0
for i in range(n):
    flavor = get_flavor(apples, i)
    diff = abs(flavor - (sum(apples) - apples[i]))
    if diff < min_diff:
        min_diff = diff
        optimal_apple = i

print(get_flavor(apples, optimal_apple))

