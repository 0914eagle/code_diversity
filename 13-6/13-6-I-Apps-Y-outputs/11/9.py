
def get_min_diff(h, w):
    # Initialize the minimum difference between the largest and smallest pieces
    min_diff = float('inf')
    
    # Loop through all possible ways to divide the bar into three pieces
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            # Check if the current division is valid
            if i + j <= h and i + j <= w:
                # Calculate the area of the largest and smallest pieces
                max_area = i * j
                min_area = (h - i) * (w - j)
                
                # Update the minimum difference
                min_diff = min(min_diff, max_area - min_area)
    
    return min_diff

def main():
    # Read the input
    h, w = map(int, input().split())
    
    # Calculate the minimum difference
    min_diff = get_min_diff(h, w)
    
    # Print the result
    print(min_diff)

if __name__ == '__main__':
    main()

