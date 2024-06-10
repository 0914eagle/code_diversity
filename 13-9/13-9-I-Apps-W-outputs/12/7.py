
def get_sorted_permutation(n, permutation):
    # Initialize the number of swaps to 0
    num_swaps = 0
    # Initialize the sorted permutation as the input permutation
    sorted_permutation = permutation
    # Loop until the permutation is sorted
    while not is_sorted(sorted_permutation):
        # Find the two indices i and j that satisfy the condition 2 * |i - j| >= n
        i, j = find_indices_to_swap(sorted_permutation, n)
        # Swap the elements at indices i and j
        sorted_permutation = swap_elements(sorted_permutation, i, j)
        # Increment the number of swaps
        num_swaps += 1
    # Return the number of swaps and the sorted permutation
    return num_swaps, sorted_permutation

def is_sorted(permutation):
    # Check if the permutation is sorted in non-decreasing order
    for i in range(len(permutation) - 1):
        if permutation[i] > permutation[i + 1]:
            return False
    return True

def find_indices_to_swap(permutation, n):
    # Find the two indices i and j that satisfy the condition 2 * |i - j| >= n
    for i in range(len(permutation)):
        for j in range(i + 1, len(permutation)):
            if abs(i - j) >= n // 2:
                return i, j
    return None, None

def swap_elements(permutation, i, j):
    # Swap the elements at indices i and j
    permutation[i], permutation[j] = permutation[j], permutation[i]
    return permutation

if __name__ == '__main__':
    n = int(input())
    permutation = list(map(int, input().split()))
    num_swaps, sorted_permutation = get_sorted_permutation(n, permutation)
    print(num_swaps)
    for i in range(num_swaps):
        print(sorted_permutation[i], sorted_permutation[i + 1])

