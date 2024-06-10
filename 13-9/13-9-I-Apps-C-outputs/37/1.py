
def get_perfect_sets(k):
    # Initialize a set to store the perfect sets
    perfect_sets = set()
    
    # Iterate from 0 to k
    for i in range(k+1):
        # Add the current number to the set
        perfect_sets.add(i)
        
        # Iterate from 0 to k
        for j in range(k+1):
            # Calculate the exclusive or of the current number and j
            xor = i ^ j
            
            # If the exclusive or is less than or equal to k, add it to the set
            if xor <= k:
                perfect_sets.add(xor)
    
    # Return the number of perfect sets
    return len(perfect_sets)

def main():
    k = int(input())
    print(get_perfect_sets(k))

if __name__ == '__main__':
    main()

