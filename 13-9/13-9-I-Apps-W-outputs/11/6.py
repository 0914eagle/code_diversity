
def get_nametag_name(k):
    # Initialize a list to store the possible names
    names = []
    
    # Iterate through all lowercase letters
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        # Calculate the absolute difference between the current letter and the next letter
        diff = abs(ord(letter) - ord(letter.upper()))
        
        # If the difference is equal to the input number, add the current letter to the list of possible names
        if diff == k:
            names.append(letter)
    
    # Return the shortest name in the list of possible names
    return sorted(names)[0]

