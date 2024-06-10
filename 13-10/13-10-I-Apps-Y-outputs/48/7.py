
def read_input():
    n = int(input())
    x = list(map(int, input().split()))
    return n, x

def find_subset(n, x):
    subset = []
    for i in range(n):
        if all(abs(x[i] - x[j]) != 2**d for j in range(n) if j != i):
            subset.append(x[i])
    return subset

def find_max_subset(n, x):
    max_subset = []
    for i in range(n):
        subset = find_subset(n - i, x[i:])
        if len(subset) > len(max_subset):
            max_subset = subset
    return max_subset

def print_output(subset):
    print(len(subset))
    print(*subset)

if __name__ == '__main__':
    n, x = read_input()
    subset = find_max_subset(n, x)
    print_output(subset)

