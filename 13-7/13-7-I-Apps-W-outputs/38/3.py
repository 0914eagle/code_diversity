
def get_amidakuji_count(H, W, K):
    # Initialize a list to store the number of valid amidakuji for each height
    height_counts = [0] * (H + 1)
    
    # Set the initial value for the first height
    height_counts[0] = 1
    
    # Iterate through each height
    for height in range(1, H + 1):
        # Initialize a list to store the number of valid amidakuji for each width
        width_counts = [0] * (W + 1)
        
        # Set the initial value for the first width
        width_counts[0] = 1
        
        # Iterate through each width
        for width in range(1, W + 1):
            # Get the number of valid amidakuji for the current height and width
            valid_count = height_counts[height - 1] * width_counts[width - 1]
            
            # Add the number of valid amidakuji for the current height and width to the total count
            height_counts[height] += valid_count
            
            # If the current width is the width of the K-th vertical line, add the number of valid amidakuji for the current height and width to the total count
            if width == K:
                height_counts[height] += valid_count
                
        # Set the number of valid amidakuji for the current height to the total count
        height_counts[height] %= 1000000007
    
    # Return the number of valid amidakuji for the last height
    return height_counts[H]

def main():
    # Read the input from stdin
    H, W, K = map(int, input().split())
    
    # Get the number of valid amidakuji that satisfy the condition
    count = get_amidakuji_count(H, W, K)
    
    # Print the number of valid amidakuji
    print(count)

if __name__ == '__main__':
    main()

