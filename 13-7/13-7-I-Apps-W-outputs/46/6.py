
def solve(essay, synonyms):
    # Initialize variables
    min_r_count = float('inf')
    min_length = float('inf')
    optimal_essay = ''

    # Iterate over all possible combinations of synonyms
    for i in range(len(synonyms)):
        for j in range(i+1, len(synonyms)):
            # Get the current essay with the synonyms replaced
            current_essay = essay.replace(synonyms[i], synonyms[j]).replace(synonyms[j], synonyms[i])

            # Count the number of 'R's in the current essay
            r_count = current_essay.lower().count('r')

            # If the current essay has fewer 'R's than the minimum, update the minimum
            if r_count < min_r_count:
                min_r_count = r_count
                min_length = len(current_essay)
                optimal_essay = current_essay

    # Return the minimum number of 'R's and the minimum length of the optimal essay
    return min_r_count, min_length

