
def get_sorted_permutation(p):
    n = len(p)
    # Initialize a list to store the swaps
    swaps = []
    # Loop through each element in the permutation
    for i in range(n):
        # Find the index of the element that is closest to its target position
        target_index = (i + 1) // 2
        # If the element is not already in its target position
        if p[i] != target_index:
            # Swap the element with the element at its target position
            swaps.append((i, target_index))
    return swaps

def perform_swaps(p, swaps):
    for i, j in swaps:
        p[i], p[j] = p[j], p[i]
    return p

def main():
    n = int(input())
    p = list(map(int, input().split()))
    swaps = get_sorted_permutation(p)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == '__main__':
    main()

