
def get_min_area_difference(height, width):
    # Initialize variables
    min_area_difference = float('inf')
    max_area = 0
    min_area = 0
    
    # Loop through all possible ways to divide the chocolate bar
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            # Calculate the area of the largest piece
            max_area = i * j
            
            # Calculate the area of the smallest piece
            min_area = (height - i) * (width - j)
            
            # Calculate the current area difference
            current_area_difference = max_area - min_area
            
            # Update the minimum area difference if necessary
            if current_area_difference < min_area_difference:
                min_area_difference = current_area_difference
    
    return min_area_difference

def main():
    height, width = map(int, input().split())
    print(get_min_area_difference(height, width))

if __name__ == '__main__':
    main()

