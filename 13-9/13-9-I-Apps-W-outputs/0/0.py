
import itertools

def get_num_strings(message):
    # Initialize a list to store the candidate strings
    candidate_strings = []
    
    # Iterate over the letters of the message
    for i in range(len(message)):
        # If the current letter is 'w', replace it with 'uu'
        if message[i] == 'w':
            message = message[:i] + 'uu' + message[i+1:]
        # If the current letter is 'm', replace it with 'nn'
        elif message[i] == 'm':
            message = message[:i] + 'nn' + message[i+1:]
    
    # Generate all possible combinations of letters for the message
    combinations = itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=len(message))
    
    # Iterate over the combinations and check if they match the message
    for combination in combinations:
        # If the current combination matches the message, add it to the list of candidate strings
        if ''.join(combination) == message:
            candidate_strings.append(combination)
    
    # Return the number of candidate strings modulo 10^9+7
    return len(candidate_strings) % (10**9+7)

