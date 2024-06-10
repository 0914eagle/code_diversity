
def get_permutation(n):
    permutation = list(range(1, n+1))
    return permutation

def get_swaps(n, m):
    swaps = []
    for i in range(m):
        a, b = map(int, input().split())
        swaps.append((a, b))
    return swaps

def get_min_swaps(permutation, swaps):
    # Initialize the minimum number of swaps to 0
    min_swaps = 0
    # Loop through each swap and check if it is valid
    for a, b in swaps:
        # If the swap is valid, perform it and increment the minimum number of swaps
        if a in permutation and b in permutation:
            permutation[permutation.index(a)], permutation[permutation.index(b)] = permutation[permutation.index(b)], permutation[permutation.index(a)]
            min_swaps += 1
    # Return the minimum number of swaps
    return min_swaps

def main():
    n, m = map(int, input().split())
    permutation = get_permutation(n)
    swaps = get_swaps(n, m)
    min_swaps = get_min_swaps(permutation, swaps)
    print(min_swaps)

if __name__ == '__main__':
    main()

