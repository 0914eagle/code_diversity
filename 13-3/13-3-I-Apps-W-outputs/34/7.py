
def solve(n, a):
    # Initialize a dictionary to store the number of occurrences of each letter
    letter_counts = {}
    for i in range(n):
        letter_counts[i] = 0
    
    # Initialize a variable to store the maximum length of the string
    max_length = 0
    
    # Loop through each letter and its corresponding limit
    for letter, limit in enumerate(a):
        # If the letter has not been used before or its limit has not been reached, add it to the string
        if letter not in letter_counts or letter_counts[letter] < limit:
            letter_counts[letter] += 1
            max_length += 1
        # If the letter has been used before and its limit has been reached, remove it from the string
        else:
            letter_counts[letter] -= 1
            max_length -= 1
    
    return max_length

