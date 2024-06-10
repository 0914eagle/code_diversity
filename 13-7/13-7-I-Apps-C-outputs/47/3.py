
def get_min_empty_squares(N):
    # Initialize variables
    min_empty_squares = N
    box_width = 1
    box_height = 1
    
    # Iterate through all possible box sizes
    while box_width <= 2 * box_height:
        # Calculate the number of widgets that can be packed in the current box
        num_widgets = box_width * box_height
        
        # If the number of widgets is greater than the number of widgets to be packed,
        # then we have found a box that is too large
        if num_widgets > N:
            break
        
        # Calculate the number of empty squares in the current box
        num_empty_squares = (box_width - N) * (box_height - N)
        
        # If the number of empty squares is less than the current minimum,
        # then update the minimum number of empty squares
        if num_empty_squares < min_empty_squares:
            min_empty_squares = num_empty_squares
        
        # Increment the box size
        box_width += 1
    
    return min_empty_squares

def main():
    N = int(input())
    print(get_min_empty_squares(N))

if __name__ == '__main__':
    main()

