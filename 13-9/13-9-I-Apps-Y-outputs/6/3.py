
def read_input():
    return map(int, input().split())

def get_flavors(n, l):
    return [l + i for i in range(1, n + 1)]

def get_optimal_flavor(n, l):
    flavors = get_flavors(n, l)
    optimal_flavor = sum(flavors[1:])
    return optimal_flavor

def main():
    n, l = read_input()
    print(get_optimal_flavor(n, l))

if __name__ == '__main__':
    main()

