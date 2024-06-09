
def solve(encrypted_message, fragment):
    # Initialize a dictionary to store the frequency of each letter in the encrypted message
    letter_freq = {}
    for letter in encrypted_message:
        if letter not in letter_freq:
            letter_freq[letter] = 1
        else:
            letter_freq[letter] += 1
    
    # Initialize a list to store the positions of the fragment in the encrypted message
    positions = []
    
    # Iterate through the encrypted message and check if the fragment is present at each position
    for i in range(len(encrypted_message) - len(fragment) + 1):
        match = True
        for j in range(len(fragment)):
            if fragment[j] != encrypted_message[i + j]:
                match = False
                break
        if match:
            positions.append(i)
    
    # If there is only one position where the fragment could occur, return the substring of the encrypted message that corresponds to the fragment
    if len(positions) == 1:
        return encrypted_message[positions[0]:positions[0] + len(fragment)]
    
    # Otherwise, return the number of positions where the fragment could occur
    else:
        return len(positions)

