
def get_even_odd_pairs(k):
    # Initialize a list to store the pairs
    pairs = []
    
    # Iterate from 1 to k
    for i in range(1, k + 1):
        # Check if i is even
        if i % 2 == 0:
            # Iterate from i+1 to k
            for j in range(i+1, k+1):
                # Check if j is odd
                if j % 2 == 1:
                    # Add the pair to the list
                    pairs.append((i, j))
    
    # Return the length of the list
    return len(pairs)

def main():
    # Read a single integer from stdin and save it in k
    k = int(input())
    
    # Call the function and save the return value in result
    result = get_even_odd_pairs(k)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

