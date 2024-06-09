
def solve(essay, synonyms):
    # Initialize variables
    min_r_count = float('inf')
    min_length = float('inf')
    opt_essay = ''

    # Iterate through all possible combinations of synonyms
    for i in range(len(synonyms)):
        for j in range(i+1, len(synonyms)):
            # Create a new essay with the current combination of synonyms
            new_essay = essay.replace(synonyms[i], synonyms[j]).replace(synonyms[j], synonyms[i])

            # Count the number of 'r's in the new essay
            r_count = new_essay.lower().count('r')

            # If the number of 'r's is less than the minimum, update the minimum and the optimal essay
            if r_count < min_r_count:
                min_r_count = r_count
                min_length = len(new_essay)
                opt_essay = new_essay

    # Return the minimum number of 'r's and the minimum length of the optimal essay
    return min_r_count, min_length

