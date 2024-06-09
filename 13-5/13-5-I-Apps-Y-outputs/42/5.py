
def get_maximum_gifts(n, k, d):
    # Initialize a list to store the pairs of boxes that can be given as gifts
    gift_pairs = []
    
    # Iterate over the boxes
    for i in range(n):
        # Check if the current box is divisible by k
        if d[i] % k == 0:
            # If the current box is divisible by k, add it to the list of gift pairs
            gift_pairs.append([i])
        else:
            # If the current box is not divisible by k, check if it can be combined with any other box to form a gift
            for j in range(i+1, n):
                if d[i] + d[j] % k == 0:
                    # If the current box can be combined with another box to form a gift, add both boxes to the list of gift pairs
                    gift_pairs.append([i, j])
                    break
    
    # Return the length of the list of gift pairs, which is the maximum number of boxes that can be given as gifts
    return len(gift_pairs)

def main():
    # Read the input data
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    
    # Call the get_maximum_gifts function and print the result
    print(get_maximum_gifts(n, k, d))

if __name__ == '__main__':
    main()

