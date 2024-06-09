
def constanze_machine(message):
    # Initialize a variable to store the number of candidate strings
    num_candidate_strings = 0
    
    # Iterate over the letters in the message
    for i in range(len(message)):
        # If the current letter is 'w', replace it with 'uu'
        if message[i] == 'w':
            message = message[:i] + 'uu' + message[i+1:]
        # If the current letter is 'm', replace it with 'nn'
        elif message[i] == 'm':
            message = message[:i] + 'nn' + message[i+1:]
    
    # Iterate over the letters in the message again
    for i in range(len(message)):
        # If the current letter is not 'w' or 'm', increment the number of candidate strings
        if message[i] not in ['w', 'm']:
            num_candidate_strings += 1
    
    # Return the number of candidate strings modulo 10^9+7
    return num_candidate_strings % (10**9+7)

