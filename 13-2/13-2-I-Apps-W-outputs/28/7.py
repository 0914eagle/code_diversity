
def get_min_operations(letter_list):
    # Initialize variables
    num_unread_letters = letter_list.count(0)
    num_operations = 0
    current_index = 0

    # Loop through the letter list
    while num_unread_letters > 0:
        # If the current letter is unread, open it
        if letter_list[current_index] == 0:
            num_unread_letters -= 1
            num_operations += 1

        # Move to the next letter
        current_index += 1

        # If we reach the end of the list, move back to the beginning
        if current_index == len(letter_list):
            current_index = 0

    return num_operations

