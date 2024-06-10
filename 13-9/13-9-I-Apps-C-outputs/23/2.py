
def are_statements_consistent(statements):
    # Initialize a dictionary to store the relationships between words
    relationships = {}
    
    # Iterate over the statements
    for statement in statements:
        # Split the statement into words
        words = statement.split()
        
        # If the statement is of the form "X is Y", add it to the dictionary
        if words[1] == "is":
            relationships[words[0]] = words[2]
        
        # If the statement is of the form "X not Y", remove Y from the dictionary
        elif words[1] == "not":
            if words[0] in relationships:
                del relationships[words[0]]
    
    # Check if the dictionary is empty, if it is, return "yes"
    if not relationships:
        return "yes"
    
    # Initialize a set to store the words that are not rhyming
    non_rhyming_words = set()
    
    # Iterate over the statements
    for statement in statements:
        # Split the statement into words
        words = statement.split()
        
        # If the statement is of the form "X is Y", check if X and Y rhyme
        if words[1] == "is":
            # Get the last 3 characters of X and Y
            x_last_3 = words[0][-3:]
            y_last_3 = words[2][-3:]
            
            # If X and Y rhyme, add them to the set of non-rhyming words
            if x_last_3 == y_last_3:
                non_rhyming_words.add(words[0])
                non_rhyming_words.add(words[2])
    
    # Check if there are any words that are not rhyming and are also related in the dictionary
    for word in non_rhyming_words:
        if word in relationships:
            return "wait what?"
    
    # If there are no conflicts, return "yes"
    return "yes"

def main():
    # Read the number of statements
    num_statements = int(input())
    
    # Read the statements
    statements = []
    for _ in range(num_statements):
        statements.append(input())
    
    # Call the function to check if the statements are consistent
    result = are_statements_consistent(statements)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

