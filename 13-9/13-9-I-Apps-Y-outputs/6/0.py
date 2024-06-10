
def get_input():
    return [int(x) for x in input().split()]

def get_flavors(n, l):
    return [l + i for i in range(1, n + 1)]

def get_min_diff(n, l):
    flavors = get_flavors(n, l)
    min_diff = abs(sum(flavors) - sum(flavors[1:]))
    for i in range(n):
        diff = abs(sum(flavors[:i] + flavors[i + 1:]) - sum(flavors))
        if diff < min_diff:
            min_diff = diff
    return min_diff

def main():
    n, l = get_input()
    print(get_min_diff(n, l))

if __name__ == '__main__':
    main()

