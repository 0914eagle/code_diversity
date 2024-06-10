
def get_perfect_sets(k):
    # Initialize a set to store the perfect sets
    perfect_sets = set()
    
    # Iterate from 0 to k
    for i in range(k+1):
        # Check if i is a perfect set
        if is_perfect_set(i):
            # Add i to the set of perfect sets
            perfect_sets.add(i)
    
    # Return the number of perfect sets modulo 1000000007
    return len(perfect_sets) % 1000000007

def is_perfect_set(n):
    # Check if n is a perfect set
    for i in range(n):
        # Check if (n xor i) is in the set of integers not greater than n
        if (n ^ i) not in range(n+1):
            return False
    return True

if __name__ == '__main__':
    k = int(input())
    print(get_perfect_sets(k))

