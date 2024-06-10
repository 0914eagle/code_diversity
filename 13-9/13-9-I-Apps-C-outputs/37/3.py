
def get_perfect_sets(k):
    # Initialize a set to store the perfect sets
    perfect_sets = set()
    
    # Iterate from 0 to k
    for i in range(k+1):
        # Initialize a set to store the elements of the current set
        curr_set = set()
        # Iterate from 0 to i
        for j in range(i+1):
            # If the current element is not in the current set, add it
            if j not in curr_set:
                curr_set.add(j)
                # If the current set is perfect, add it to the perfect sets
                if is_perfect(curr_set):
                    perfect_sets.add(frozenset(curr_set))
    
    # Return the number of perfect sets modulo 1000000007
    return len(perfect_sets) % 1000000007

def is_perfect(s):
    # Iterate over all pairs of elements in the set
    for i in s:
        for j in s:
            # If the exclusive or of the two elements is not in the set, return False
            if i ^ j not in s:
                return False
    
    # If all pairs of elements have an exclusive or in the set, return True
    return True

if __name__ == '__main__':
    k = int(input())
    print(get_perfect_sets(k))

