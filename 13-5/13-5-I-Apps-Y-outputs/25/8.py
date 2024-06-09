
def solve(box_number, questions):
    # Initialize a list to store the player numbers
    player_numbers = list(range(1, 9))
    # Remove the player with the box from the list
    player_numbers.remove(box_number)
    # Iterate through the questions
    for question in questions:
        # If the answer is correct, move the box to the next player
        if question[1] == "T":
            box_number = player_numbers[player_numbers.index(box_number) - 1]
        # If the answer is incorrect or skipped, move the box to the next player
        else:
            box_number = player_numbers[player_numbers.index(box_number) + 1]
    # Return the player number with the box
    return box_number

