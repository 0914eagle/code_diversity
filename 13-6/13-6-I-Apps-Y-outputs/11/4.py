
def get_min_diff(H, W):
    # Initialize the minimum difference between the largest and smallest pieces
    min_diff = float('inf')
    
    # Loop through all possible ways to divide the chocolate bar
    for i in range(1, H):
        for j in range(1, W):
            # Check if the current division is valid
            if H % i == 0 and W % j == 0:
                # Calculate the area of the largest piece
                max_area = H // i * j
                # Calculate the area of the smallest piece
                min_area = (H // i - 1) * (W // j - 1)
                # Calculate the current difference between the largest and smallest pieces
                current_diff = max_area - min_area
                # Update the minimum difference if necessary
                min_diff = min(min_diff, current_diff)
    
    # Return the minimum difference
    return min_diff

def main():
    # Read the input
    H, W = map(int, input().split())
    # Call the function to get the minimum difference
    min_diff = get_min_diff(H, W)
    # Print the result
    print(min_diff)

if __name__ == '__main__':
    main()

