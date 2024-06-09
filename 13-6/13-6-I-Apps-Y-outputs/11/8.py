
def get_min_diff(h, w):
    # Initialize the minimum difference between the largest and smallest pieces
    min_diff = float('inf')
    
    # Loop through all possible positions for the cut
    for i in range(h):
        for j in range(w):
            # Get the area of the largest piece
            max_area = h * w - (i * w + j)
            
            # Get the area of the smallest piece
            min_area = i * w + j
            
            # Update the minimum difference
            min_diff = min(min_diff, max_area - min_area)
    
    return min_diff

def main():
    # Read the input
    h, w = map(int, input().split())
    
    # Call the function to get the minimum difference
    min_diff = get_min_diff(h, w)
    
    # Print the result
    print(min_diff)

if __name__ == '__main__':
    main()

