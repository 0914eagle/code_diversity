
def solve(n, a):
    # Initialize a dictionary to store the number of occurrences of each letter
    letter_counts = {}
    for i in range(n):
        letter_counts[i] = 0
    
    # Initialize a variable to store the maximum length of the string
    max_length = 0
    
    # Loop through each letter and its corresponding limit
    for letter, limit in enumerate(a):
        # If the limit is 0, skip this letter
        if limit == 0:
            continue
        
        # If the letter has already occurred in the string, decrease its limit by 1
        if letter_counts[letter] > 0:
            limit -= 1
        
        # If the limit is still positive, add the letter to the string
        if limit > 0:
            letter_counts[letter] += 1
            max_length += 1
    
    # Return the maximum length of the string
    return max_length

