
def get_number_of_empty_squares(number_of_widgets):
    # Initialize a list to store the dimensions of the boxes
    box_dimensions = []
    
    # Loop through all possible box dimensions
    for width in range(1, number_of_widgets + 1):
        for height in range(1, number_of_widgets + 1):
            # Check if the box dimensions are valid
            if height / 2 <= width <= 2 * height:
                # Add the box dimensions to the list
                box_dimensions.append((width, height))
    
    # Initialize a list to store the number of empty squares for each box dimension
    number_of_empty_squares = []
    
    # Loop through all possible box dimensions
    for width, height in box_dimensions:
        # Calculate the number of empty squares for the current box dimension
        number_of_empty_squares.append(width * height - number_of_widgets)
    
    # Return the minimum number of empty squares
    return min(number_of_empty_squares)

def main():
    # Read the number of widgets to be packed from stdin
    number_of_widgets = int(input())
    
    # Call the get_number_of_empty_squares function and print the result
    print(get_number_of_empty_squares(number_of_widgets))

if __name__ == '__main__':
    main()

