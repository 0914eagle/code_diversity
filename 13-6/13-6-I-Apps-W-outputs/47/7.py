
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
    # Otherwise, return the set
    return even_indices

def get_even_subset_with_duplicates(a):
    # Initialize a dictionary to store the count of each element
    element_count = {}
    # Initialize a set to store the indices of the elements with even sum
    even_indices = set()
    # Iterate through the array
    for i, x in enumerate(a):
        # If the current element is not in the dictionary, add it to the dictionary with count 1
        if x not in element_count:
            element_count[x] = 1
        # Otherwise, increment the count of the element
        else:
            element_count[x] += 1
        # If the count of the element is even, add its index to the set
        if element_count[x] % 2 == 0:
            even_indices.add(i)
    # If the set is empty, return -1
    if not even_indices:
        return -1
    # Otherwise, return the set
    return even_indices

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        result = get_even_subset_with_duplicates(a)
        if result == -1:
            print(-1)
        else:
            print(len(result))
            print(*result)

