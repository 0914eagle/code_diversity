
def read_input():
    n = int(input())
    x = list(map(int, input().split()))
    return n, x

def solve(n, x):
    x.sort()
    max_subset = []
    for i in range(n):
        current_subset = [x[i]]
        for j in range(i+1, n):
            if x[j] - x[i] == 2**len(current_subset):
                current_subset.append(x[j])
        if len(current_subset) > len(max_subset):
            max_subset = current_subset
    return len(max_subset), max_subset

def print_output(n, x):
    m, max_subset = solve(n, x)
    print(m)
    print(*max_subset)

if __name__ == '__main__':
    n, x = read_input()
    print_output(n, x)

