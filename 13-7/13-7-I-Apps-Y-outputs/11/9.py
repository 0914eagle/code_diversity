
def get_subset(n, x):
    # Sort the array
    x.sort()
    
    # Initialize variables
    m = 1
    subset = [x[0]]
    
    # Iterate over the array
    for i in range(1, n):
        # Check if the current element is a power of two away from the last element in the subset
        if x[i] - subset[-1] == 2**m:
            # If it is, add it to the subset and increment the power of two
            subset.append(x[i])
            m += 1
        else:
            # If it's not, return the current subset
            return subset
    
    # Return the final subset
    return subset

def main():
    # Read the input
    n = int(input())
    x = list(map(int, input().split()))
    
    # Get the subset
    subset = get_subset(n, x)
    
    # Print the size of the subset
    print(len(subset))
    
    # Print the subset
    print(" ".join(str(x) for x in subset))

if __name__ == '__main__':
    main()

