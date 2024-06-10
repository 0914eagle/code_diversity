
def get_permutation(N, M):
    # Function to get the permutation of numbers 1 to N
    permutation = list(range(1, N+1))
    for i in range(M):
        a, b = map(int, input().split())
        permutation[a-1], permutation[b-1] = permutation[b-1], permutation[a-1]
    return permutation

def get_swaps(permutation):
    # Function to get the minimum number of swaps to transform the permutation to 1, 2, ..., N
    swaps = 0
    for i in range(len(permutation)):
        if permutation[i] != i+1:
            swaps += 1
    return swaps

def main():
    N, M = map(int, input().split())
    permutation = get_permutation(N, M)
    print(get_swaps(permutation))

if __name__ == '__main__':
    main()

