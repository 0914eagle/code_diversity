
def is_rhyming(word1, word2):
    return word1[-min(3, len(word1), len(word2)):].lower() == word2[-min(3, len(word1), len(word2)):].lower()

def is_consistent(statements):
    # Initialize a dictionary to store the rhyming pairs
    rhyming_pairs = {}
    # Iterate over the statements
    for statement in statements:
        # Split the statement into two words
        word1, word2 = statement.split()
        # Check if the two words are already in the dictionary
        if word1 in rhyming_pairs and rhyming_pairs[word1] != word2:
            # If they are, and they don't have the same rhyming pair, return "wait what?"
            return "wait what?"
        # If the two words are not in the dictionary, add them to the dictionary with their rhyming pair
        rhyming_pairs[word1] = word2
        rhyming_pairs[word2] = word1
    # If we reach this point, all statements are consistent
    return "yes"

def main():
    # Read the number of statements
    num_statements = int(input())
    # Read the statements
    statements = [input() for _ in range(num_statements)]
    # Call the is_consistent function
    result = is_consistent(statements)
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

