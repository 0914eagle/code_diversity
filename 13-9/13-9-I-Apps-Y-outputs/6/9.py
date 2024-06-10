
def get_input():
    return list(map(int, input().split()))

def get_flavors(N, L):
    return [L + i - 1 for i in range(1, N + 1)]

def get_optimal_choice(flavors):
    return min(flavors, key=lambda x: abs(sum(flavors) - x - sum(flavors[1:])))

def get_flavor_of_remaining_apples(flavors, optimal_choice):
    return sum(flavors[1:]) - optimal_choice

def main():
    N, L = get_input()
    flavors = get_flavors(N, L)
    optimal_choice = get_optimal_choice(flavors)
    flavor_of_remaining_apples = get_flavor_of_remaining_apples(flavors, optimal_choice)
    print(flavor_of_remaining_apples)

if __name__ == '__main__':
    main()

