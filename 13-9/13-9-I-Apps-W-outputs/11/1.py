
def solve(k):
    # Initialize the dictionary to map each letter to its position in the alphabet
    letter_map = {chr(i): i - 96 for i in range(97, 123)}
    
    # Initialize the minimum length of the string as infinity
    min_len = float('inf')
    
    # Initialize the string that encodes to the minimum length as empty string
    min_string = ""
    
    # Iterate over all possible strings of length 1 to k
    for i in range(1, k+1):
        for j in range(97, 123):
            # Get the letter at the current position
            letter = chr(j)
            
            # Get the value of the letter
            value = letter_map[letter]
            
            # If the value is equal to the current number, update the minimum length and the minimum string
            if value == i:
                min_len = 1
                min_string = letter
                break
            
            # If the value is greater than the current number, update the minimum length and the minimum string
            elif value > i:
                min_len = i
                min_string = letter
                break
    
    # Return the minimum string
    return min_string

