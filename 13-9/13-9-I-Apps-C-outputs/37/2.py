
def get_perfect_sets(k):
    # Initialize a set to store the perfect sets
    perfect_sets = set()
    
    # Iterate from 0 to k
    for i in range(k+1):
        # Check if i is a perfect set
        if is_perfect_set(i):
            # Add i to the perfect sets
            perfect_sets.add(i)
    
    # Return the number of perfect sets
    return len(perfect_sets)

def is_perfect_set(n):
    # Initialize a set to store the elements of n
    elements = set()
    
    # Iterate from 0 to n
    for i in range(n+1):
        # Check if i is a perfect set
        if n & (1 << i):
            # Add i to the elements
            elements.add(i)
    
    # Return True if n is a perfect set, False otherwise
    return len(elements) == 2

if __name__ == '__main__':
    k = int(input())
    print(get_perfect_sets(k))

