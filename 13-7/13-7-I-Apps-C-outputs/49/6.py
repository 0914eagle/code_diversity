
def get_initial_permutation(n):
    permutation = list(range(1, n+1))
    return permutation

def get_allowed_swaps(m):
    allowed_swaps = []
    for i in range(m):
        a, b = map(int, input().split())
        allowed_swaps.append((a, b))
    return allowed_swaps

def get_minimum_swaps(permutation, allowed_swaps):
    swaps = 0
    for i in range(len(permutation)):
        if permutation[i] != i+1:
            swaps += 1
    return swaps

def perform_swaps(permutation, allowed_swaps):
    for swap in allowed_swaps:
        a, b = swap
        permutation[a-1], permutation[b-1] = permutation[b-1], permutation[a-1]
    return permutation

def main():
    n, m = map(int, input().split())
    permutation = get_initial_permutation(n)
    allowed_swaps = get_allowed_swaps(m)
    minimum_swaps = get_minimum_swaps(permutation, allowed_swaps)
    print(minimum_swaps)

if __name__ == '__main__':
    main()

