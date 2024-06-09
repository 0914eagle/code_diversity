
def get_maximal_factoring_weight(string):
    # Initialize a dictionary to store the factorings and their weights
    factorings = {}
    
    # Iterate over the length of the string
    for length in range(1, len(string) + 1):
        # Iterate over the starting indices of the substring
        for start in range(len(string) - length + 1):
            # Get the substring
            substring = string[start:start + length]
            # Check if the substring is already in the dictionary
            if substring in factorings:
                # If it is, update the weight of the factoring
                factorings[substring] += 1
            else:
                # If it's not, add it to the dictionary with weight 1
                factorings[substring] = 1
    
    # Find the maximal factoring with the smallest weight
    maximal_factoring = min(factorings, key=factorings.get)
    
    # Return the weight of the maximal factoring
    return factorings[maximal_factoring]

