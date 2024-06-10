
def get_permutation(n, m):
    # Function to get the permutation of numbers 1 to n
    permutation = list(range(1, n+1))
    for i in range(m):
        a, b = map(int, input().split())
        permutation[a-1], permutation[b-1] = permutation[b-1], permutation[a-1]
    return permutation

def get_swaps(permutation):
    # Function to get the minimum number of swaps to transform the permutation to 1, 2, ..., n
    n = len(permutation)
    swaps = 0
    for i in range(n):
        if permutation[i] != i+1:
            swaps += 1
    return swaps

def main():
    n, m = map(int, input().split())
    permutation = get_permutation(n, m)
    print(get_swaps(permutation))

if __name__ == '__main__':
    main()

