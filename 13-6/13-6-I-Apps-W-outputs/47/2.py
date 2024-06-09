
def get_even_subset(a):
    # Initialize a set to store the indices of the elements with even sum
    even_indices = set()
    # Iterate through the array
    for i, x in enumerate(a):
        # If the current element is even, add its index to the set
        if x % 2 == 0:
            even_indices.add(i)
    # If the set is empty, return -1
    if not even_indices:
        return -1
    # Otherwise, return the set of indices
    return even_indices

def get_even_subset_with_min_size(a, k):
    # Initialize a set to store the indices of the elements with even sum
    even_indices = set()
    # Iterate through the array
    for i, x in enumerate(a):
        # If the current element is even, add its index to the set
        if x % 2 == 0:
            even_indices.add(i)
    # If the set is empty, return -1
    if not even_indices:
        return -1
    # Otherwise, return the set of indices
    return even_indices

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_even_subset(a))
        k = int(input())
        print(get_even_subset_with_min_size(a, k))

