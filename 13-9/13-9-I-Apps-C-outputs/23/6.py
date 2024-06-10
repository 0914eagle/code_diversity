
def is_rhyming(word1, word2):
    # Find the minimum of 3, length of word1, and length of word2
    min_len = min(3, len(word1), len(word2))
    # Check if the last min_len characters of word1 and word2 are the same
    return word1[-min_len:] == word2[-min_len:]

def is_consistent(statements):
    # Create a dictionary to store the relationships between words
    relationships = {}
    # Iterate over the statements
    for statement in statements:
        # Split the statement into words
        word1, word2 = statement.split()
        # Check if the words are already in the dictionary
        if word1 in relationships and relationships[word1] != word2:
            # If they are and the values are not the same, return "wait what?"
            return "wait what?"
        elif word2 in relationships and relationships[word2] != word1:
            # If they are and the values are not the same, return "wait what?"
            return "wait what?"
        # Add the relationship to the dictionary
        relationships[word1] = word2
        relationships[word2] = word1
    # If all statements are consistent, return "yes"
    return "yes"

def main():
    # Read the number of statements
    num_statements = int(input())
    # Read the statements
    statements = [input() for _ in range(num_statements)]
    # Check if the statements are consistent
    result = is_consistent(statements)
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

