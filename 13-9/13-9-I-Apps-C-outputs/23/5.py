
def is_consistent(statements):
    # Create a dictionary to store the relationships between words
    relationships = {}
    
    # Iterate over the statements and populate the dictionary
    for statement in statements:
        # Split the statement into words
        words = statement.split()
        
        # Get the first and second words
        word1, word2 = words[0], words[2]
        
        # If the statement is in the form "X is Y", add the relationship to the dictionary
        if words[1] == "is":
            relationships[word1] = word2
        # If the statement is in the form "X not Y", remove the relationship from the dictionary
        elif words[1] == "not":
            if word1 in relationships:
                del relationships[word1]
    
    # Check if all relationships are consistent
    for word1, word2 in relationships.items():
        # Check if the last 3 characters of the two words are the same
        if word1[-3:] == word2[-3:]:
            return "yes"
    
    return "wait what?"

def main():
    # Read the number of statements
    num_statements = int(input())
    
    # Read the statements
    statements = []
    for _ in range(num_statements):
        statements.append(input())
    
    # Call the is_consistent function and print the result
    result = is_consistent(statements)
    print(result)

if __name__ == '__main__':
    main()

