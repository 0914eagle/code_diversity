
def find_match(encrypted_message, decrypted_fragment):
    # Initialize a dictionary to store the number of occurrences of each letter in the encrypted message
    letter_counts = {}
    for letter in encrypted_message:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    
    # Initialize a variable to store the number of positions in the encrypted message where the fragment could occur
    num_positions = 0
    
    # Iterate through the encrypted message and check if the fragment could occur at each position
    for i in range(len(encrypted_message)):
        # If the letter at the current position is not in the fragment, skip to the next position
        if encrypted_message[i] not in decrypted_fragment:
            continue
        
        # If the letter at the current position is in the fragment, check if the fragment could occur at this position
        if encrypted_message[i:i+len(decrypted_fragment)] == decrypted_fragment:
            # If the fragment could occur at this position, increment the number of positions where it could occur
            num_positions += 1
    
    # If the number of positions where the fragment could occur is 1, return the substring of the encrypted message that could correspond to the fragment
    if num_positions == 1:
        return encrypted_message[i:i+len(decrypted_fragment)]
    # Otherwise, return the number of positions where the fragment could occur
    else:
        return num_positions

