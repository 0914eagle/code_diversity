
def read_input():
    return [int(x) for x in input().split()]

def get_flavors(L, N):
    return [L + i for i in range(1, N + 1)]

def get_best_apple(flavors):
    return min(flavors, key=lambda x: abs(sum(flavors) - x))

def get_remaining_flavors(flavors, best_apple):
    return [f for f in flavors if f != best_apple]

def get_remaining_flavor_sum(flavors, best_apple):
    return sum(get_remaining_flavors(flavors, best_apple))

def solve(L, N):
    flavors = get_flavors(L, N)
    best_apple = get_best_apple(flavors)
    return get_remaining_flavor_sum(flavors, best_apple)

if __name__ == '__main__':
    L, N = read_input()
    print(solve(L, N))

