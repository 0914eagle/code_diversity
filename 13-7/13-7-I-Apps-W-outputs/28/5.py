
def get_correct_fields(field):
    # Initialize a list to store the correct fields
    correct_fields = []
    
    # Loop through each cell in the field
    for i in range(len(field)):
        # If the current cell is a question mark, then we have to check all possible options
        if field[i] == "?":
            # Loop through all possible options (0, 1, 2)
            for option in range(3):
                # Create a copy of the current field
                new_field = field[:]
                # Replace the question mark with the current option
                new_field[i] = str(option)
                # Check if the new field is correct
                if is_correct_field(new_field):
                    # If the new field is correct, then add it to the list of correct fields
                    correct_fields.append(new_field)
        # If the current cell is not a question mark, then we don't have to check any options
        else:
            # Create a copy of the current field
            new_field = field[:]
            # Check if the new field is correct
            if is_correct_field(new_field):
                # If the new field is correct, then add it to the list of correct fields
                correct_fields.append(new_field)
    
    # Return the number of correct fields
    return len(correct_fields)

def is_correct_field(field):
    # Initialize a variable to store the number of bombs
    num_bombs = 0
    
    # Loop through each cell in the field
    for i in range(len(field)):
        # If the current cell is a bomb, then increment the number of bombs
        if field[i] == "*":
            num_bombs += 1
        # If the current cell is a number, then check if it is correct
        elif field[i].isdigit():
            # If the number is not correct, then return False
            if not is_correct_number(field, i):
                return False
    
    # If the number of bombs is not correct, then return False
    if num_bombs != get_num_bombs(field):
        return False
    
    # If the field is correct, then return True
    return True

def is_correct_number(field, index):
    # Initialize a variable to store the number of adjacent bombs
    num_adjacent_bombs = 0
    
    # Loop through the adjacent cells
    for i in range(index-1, index+2):
        # If the current cell is a bomb, then increment the number of adjacent bombs
        if field[i] == "*":
            num_adjacent_bombs += 1
    
    # If the number of adjacent bombs is not equal to the current cell, then return False
    if num_adjacent_bombs != int(field[index]):
        return False
    
    # If the number is correct, then return True
    return True

def get_num_bombs(field):
    # Initialize a variable to store the number of bombs
    num_bombs = 0
    
    # Loop through each cell in the field
    for i in range(len(field)):
        # If the current cell is a bomb, then increment the number of bombs
        if field[i] == "*":
            num_bombs += 1
    
    # Return the number of bombs
    return num_bombs

if __name__ == '__main__':
    field = input()
    print(get_correct_fields(field) % 1000000007)

