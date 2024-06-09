
def f1(essay, synonyms):
    # Initialize variables
    min_r_count = float('inf')
    min_length = float('inf')
    optimal_essay = ''

    # Iterate through all possible combinations of synonyms
    for i in range(len(synonyms)):
        for j in range(i+1, len(synonyms)):
            # Replace words with their synonyms
            new_essay = essay.replace(synonyms[i], synonyms[j])
            new_essay = new_essay.replace(synonyms[j], synonyms[i])

            # Count the number of 'r's in the new essay
            r_count = new_essay.lower().count('r')

            # If the number of 'r's is less than the minimum, update the minimum
            if r_count < min_r_count:
                min_r_count = r_count
                min_length = len(new_essay)
                optimal_essay = new_essay

    return min_r_count, min_length, optimal_essay

def f2(essay, synonyms):
    # Initialize variables
    min_r_count = float('inf')
    min_length = float('inf')
    optimal_essay = ''

    # Iterate through all possible combinations of synonyms
    for i in range(len(synonyms)):
        for j in range(i+1, len(synonyms)):
            # Replace words with their synonyms
            new_essay = essay.replace(synonyms[i], synonyms[j])
            new_essay = new_essay.replace(synonyms[j], synonyms[i])

            # Count the number of 'r's in the new essay
            r_count = new_essay.lower().count('r')

            # If the number of 'r's is less than the minimum, update the minimum
            if r_count < min_r_count:
                min_r_count = r_count
                min_length = len(new_essay)
                optimal_essay = new_essay

    return min_r_count, min_length, optimal_essay

if __name__ == '__main__':
    essay = input()
    synonyms = input()
    min_r_count, min_length, optimal_essay = f1(essay, synonyms)
    print(min_r_count, min_length)

