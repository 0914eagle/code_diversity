
def get_flavors(n, l):
    flavors = []
    for i in range(1, n+1):
        flavors.append(l+i-1)
    return flavors

def get_optimal_flavor(n, l):
    flavors = get_flavors(n, l)
    optimal_flavor = sum(flavors[1:])
    return optimal_flavor

def get_remaining_flavor(n, l):
    flavors = get_flavors(n, l)
    remaining_flavors = flavors[:n-1]
    remaining_flavor = sum(remaining_flavors)
    return remaining_flavor

def main():
    n, l = map(int, input().split())
    optimal_flavor = get_optimal_flavor(n, l)
    remaining_flavor = get_remaining_flavor(n, l)
    print(remaining_flavor)

if __name__ == '__main__':
    main()

