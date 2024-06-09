
def get_min_diff(H, W):
    # Initialize the minimum difference between the largest and smallest pieces
    min_diff = float('inf')
    
    # Loop through all possible ways to divide the chocolate bar
    for i in range(1, H):
        for j in range(1, W):
            # If the height and width are not equal, skip this division
            if i != j:
                continue
            
            # Calculate the area of the largest piece
            largest_piece = i * W
            
            # Calculate the area of the smallest piece
            smallest_piece = (H - i) * (W - j)
            
            # Calculate the current difference between the largest and smallest pieces
            current_diff = largest_piece - smallest_piece
            
            # Update the minimum difference if necessary
            if current_diff < min_diff:
                min_diff = current_diff
    
    # Return the minimum difference
    return min_diff

def main():
    # Read the input data
    H, W = map(int, input().split())
    
    # Calculate the minimum difference
    min_diff = get_min_diff(H, W)
    
    # Print the result
    print(min_diff)

if __name__ == '__main__':
    main()

