
def count_perfect_sets(k):
    # Initialize a set to store the perfect sets
    perfect_sets = set()
    
    # Iterate from 0 to k
    for i in range(k+1):
        # Add the current number to the perfect sets
        perfect_sets.add(i)
        # Iterate from 0 to k-1
        for j in range(i):
            # Calculate the exclusive or of the current number and j
            xor = i ^ j
            # If the exclusive or is less than or equal to k, add it to the perfect sets
            if xor <= k:
                perfect_sets.add(xor)
    
    # Return the number of perfect sets modulo 1000000007
    return len(perfect_sets) % 1000000007

def main():
    # Read the input k
    k = int(input())
    # Calculate the number of perfect sets
    count = count_perfect_sets(k)
    # Print the number of perfect sets modulo 1000000007
    print(count)

if __name__ == '__main__':
    main()

