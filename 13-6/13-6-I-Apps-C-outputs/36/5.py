
def decrypt_message(encrypted_message, fragment):
    # Initialize a dictionary to store the number of occurrences of each letter in the fragment
    letter_counts = {}
    for letter in fragment:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1

    # Initialize a variable to store the number of positions where the fragment could occur
    num_positions = 0

    # Iterate through the encrypted message
    for i in range(len(encrypted_message)):
        # Check if the letter at the current position is in the fragment
        if encrypted_message[i] in letter_counts:
            # Decrement the count of the letter in the fragment
            letter_counts[encrypted_message[i]] -= 1

            # If the count is 0, it means that the letter has been found in the encrypted message
            if letter_counts[encrypted_message[i]] == 0:
                # Increment the number of positions where the fragment could occur
                num_positions += 1

                # If all letters in the fragment have been found, return the substring
                if len(letter_counts) == 0:
                    return encrypted_message[i-num_positions+1:i+1]

    # If not all letters in the fragment have been found, return the number of positions where the fragment could occur
    return num_positions

