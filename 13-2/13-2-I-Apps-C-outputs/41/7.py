
def find_maximal_factoring(string):
    # Initialize a dictionary to store the factorings and their weights
    factorings = {}
    
    # Loop through each substring of the string
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            # Check if the substring is a prefix of the string
            if string[:j] == string[i:j]:
                # If it is, add it to the dictionary with its weight
                factorings[string[i:j]] = j - i
    
    # Find the maximal factoring with the smallest weight
    return min(factorings, key=factorings.get)

