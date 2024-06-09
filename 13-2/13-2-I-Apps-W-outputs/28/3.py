
def get_min_operations(n, letters):
    # Initialize variables
    operations = 0
    current_letter = 0
    read_letters = 0

    # Iterate through the letters
    for letter in letters:
        # If the letter is unread, open it
        if letter == 0:
            operations += 1
            read_letters += 1
        # If the letter is read, move to the next letter
        else:
            operations += 1
            current_letter += 1

    # Return the minimum number of operations needed to read all unread letters
    return operations + (n - read_letters)

