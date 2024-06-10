
def read_input():
    N, M = map(int, input().split())
    permutation = list(map(int, input().split()))
    allowed_swaps = []
    for _ in range(M):
        A, B = map(int, input().split())
        allowed_swaps.append((A, B))
    return N, M, permutation, allowed_swaps

def get_min_swaps(N, M, permutation, allowed_swaps):
    # Initialize a dictionary to store the number of swaps needed for each element
    swaps_needed = {i: 0 for i in range(1, N + 1)}
    
    # Initialize a set to store the elements that have been swapped
    swapped_elements = set()
    
    # Loop through the allowed swaps and update the swaps needed for each element
    for A, B in allowed_swaps:
        if A not in swapped_elements and B not in swapped_elements:
            swapped_elements.add(A)
            swapped_elements.add(B)
            swaps_needed[A] += 1
            swaps_needed[B] += 1
    
    # Return the minimum number of swaps needed
    return min(swaps_needed.values())

def main():
    N, M, permutation, allowed_swaps = read_input()
    print(get_min_swaps(N, M, permutation, allowed_swaps))

if __name__ == '__main__':
    main()

