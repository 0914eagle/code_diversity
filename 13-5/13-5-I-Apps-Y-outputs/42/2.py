
def get_max_gifts(d, k):
    # Initialize a list to store the pairs of boxes that can be given as gifts
    gift_pairs = []
    
    # Iterate over the boxes
    for i in range(len(d)):
        # Check if the current box can be given as a gift
        if d[i] % k == 0:
            # If the current box can be given as a gift, add it to the list of gift pairs
            gift_pairs.append([i, i])
        else:
            # If the current box cannot be given as a gift, check if it can be combined with any other box to form a gift
            for j in range(i+1, len(d)):
                if d[i] + d[j] % k == 0:
                    # If the current box can be combined with another box to form a gift, add the pair of boxes to the list of gift pairs
                    gift_pairs.append([i, j])
                    break
    
    # Return the maximum number of gift pairs that can be formed
    return len(gift_pairs)

def main():
    # Read the input data
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    
    # Call the get_max_gifts function to get the maximum number of gifts that can be formed
    max_gifts = get_max_gifts(d, k)
    
    # Print the maximum number of gifts that can be formed
    print(max_gifts)

if __name__ == '__main__':
    main()

