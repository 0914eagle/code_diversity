
def get_correct_fields(field):
    # Initialize a list to store the correct fields
    correct_fields = []
    
    # Loop through each cell in the field
    for i in range(len(field)):
        # If the current cell is a question mark, we have to find all possible combinations of bombs and numbers
        if field[i] == "?":
            # Get the indices of the adjacent cells
            adjacents = get_adjacent_indices(i, len(field))
            
            # Loop through each possible combination of bombs and numbers
            for num_bombs in range(0, 3):
                for num_numbers in range(0, 3):
                    # Check if the current combination is valid
                    if is_valid_combination(field, adjacents, num_bombs, num_numbers):
                        # If the combination is valid, add it to the list of correct fields
                        correct_fields.append(get_correct_field(field, i, num_bombs, num_numbers))
    
    # Return the number of correct fields
    return len(correct_fields)

def get_adjacent_indices(index, size):
    # Get the indices of the adjacent cells
    adjacents = []
    if index > 0:
        adjacents.append(index - 1)
    if index < size - 1:
        adjacents.append(index + 1)
    return adjacents

def is_valid_combination(field, adjacents, num_bombs, num_numbers):
    # Check if the current combination is valid
    if num_bombs + num_numbers != 2:
        return False
    if num_bombs > len(adjacents):
        return False
    if num_numbers > len(adjacents) - num_bombs:
        return False
    for i in range(len(adjacents)):
        if field[adjacents[i]] == "*":
            if num_bombs == 0:
                return False
            num_bombs -= 1
        elif field[adjacents[i]].isdigit():
            if num_numbers == 0:
                return False
            num_numbers -= 1
    return True

def get_correct_field(field, index, num_bombs, num_numbers):
    # Get the correct field
    correct_field = field[:]
    correct_field[index] = str(num_bombs)
    for i in range(len(adjacents)):
        if adjacents[i] != index:
            if num_bombs > 0:
                correct_field[adjacents[i]] = "*"
                num_bombs -= 1
            elif num_numbers > 0:
                correct_field[adjacents[i]] = str(num_numbers)
                num_numbers -= 1
    return correct_field

if __name__ == '__main__':
    field = input()
    print(get_correct_fields(field))

