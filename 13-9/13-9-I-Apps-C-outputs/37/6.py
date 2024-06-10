
def is_perfect(s):
    # Check if the set is empty
    if not s:
        return False
    
    # Check if the set contains only non-negative integers
    if any(x < 0 for x in s):
        return False
    
    # Check if the set is perfect
    for a in s:
        for b in s:
            if a != b and (a ^ b) not in s:
                return False
    
    return True

def count_perfect_sets(k):
    # Initialize a set to store the perfect sets
    perfect_sets = set()
    
    # Iterate from 0 to k
    for i in range(k+1):
        # Add the current number to the set
        s = {i}
        
        # Check if the set is perfect
        if is_perfect(s):
            # Add the set to the list of perfect sets
            perfect_sets.add(frozenset(s))
    
    # Return the number of perfect sets modulo 1000000007
    return len(perfect_sets) % 1000000007

if __name__ == '__main__':
    k = int(input())
    print(count_perfect_sets(k))

