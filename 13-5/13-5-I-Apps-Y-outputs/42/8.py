
def get_max_gifts(n, k, d):
    # Initialize a list to store the pairs of boxes that can be given as gifts
    gift_pairs = []
    
    # Iterate over the boxes
    for i in range(n):
        # Check if the current box is divisible by k
        if d[i] % k == 0:
            # If it is, add it to the list of gift pairs
            gift_pairs.append((i,))
        else:
            # If it is not, check if it can be combined with any other box to form a pair that is divisible by k
            for j in range(i+1, n):
                if (d[i] + d[j]) % k == 0:
                    # If it can, add the pair to the list of gift pairs
                    gift_pairs.append((i, j))
                    break
    
    # Return the length of the list of gift pairs, which is the maximum number of boxes that can be given as gifts
    return len(gift_pairs)

def main():
    # Read the input data
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    
    # Call the function to get the maximum number of gifts that can be given
    max_gifts = get_max_gifts(n, k, d)
    
    # Print the result
    print(max_gifts)

if __name__ == '__main__':
    main()

