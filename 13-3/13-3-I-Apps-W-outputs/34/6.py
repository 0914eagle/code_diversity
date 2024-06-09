
def max_string_length(n, a):
    # Initialize a dictionary to store the number of occurrences of each letter
    letter_counts = {}
    for i in range(n):
        letter_counts[i] = 0
    
    # Initialize a variable to store the maximum length of the string
    max_length = 0
    
    # Iterate through the letters of the alphabet
    for letter in range(n):
        # If the letter has not been used yet, use it in the string
        if letter_counts[letter] == 0:
            max_length += 1
            letter_counts[letter] += 1
        # If the letter has already been used, check if it can be used again
        elif letter_counts[letter] < a[letter]:
            max_length += 1
            letter_counts[letter] += 1
    
    return max_length

