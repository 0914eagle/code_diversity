
def read_input():
    N, L = map(int, input().split())
    return N, L

def get_apple_flavors(N, L):
    apple_flavors = []
    for i in range(1, N+1):
        apple_flavors.append(L+i-1)
    return apple_flavors

def get_optimal_flavor(apple_flavors):
    optimal_flavor = 0
    for i in range(1, len(apple_flavors)):
        optimal_flavor += apple_flavors[i]
    return optimal_flavor

def get_flavor_with_one_apple_less(apple_flavors):
    flavor_with_one_apple_less = 0
    for i in range(1, len(apple_flavors)-1):
        flavor_with_one_apple_less += apple_flavors[i]
    return flavor_with_one_apple_less

def solve(N, L):
    apple_flavors = get_apple_flavors(N, L)
    optimal_flavor = get_optimal_flavor(apple_flavors)
    flavor_with_one_apple_less = get_flavor_with_one_apple_less(apple_flavors)
    return optimal_flavor - flavor_with_one_apple_less

if __name__ == '__main__':
    N, L = read_input()
    print(solve(N, L))

