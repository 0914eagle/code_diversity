
def get_maximal_factoring_weight(string):
    # Initialize a dictionary to store the factorings and their weights
    factorings = {}
    
    # Loop through each substring of the string
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            # Check if the substring is a factor of the string
            if string[i:j] in string:
                # If it is, add it to the dictionary with its weight
                factorings[string[i:j]] = j - i
    
    # Find the maximal factoring with the smallest weight
    maximal_factoring = min(factorings, key=factorings.get)
    
    # Return the weight of the maximal factoring
    return factorings[maximal_factoring]

