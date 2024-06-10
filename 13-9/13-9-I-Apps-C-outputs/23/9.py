
def is_consistent(statements):
    # Initialize a dictionary to store the rhyming relationships
    rhyming_dict = {}
    
    # Iterate through the statements
    for statement in statements:
        # Split the statement into words
        words = statement.split()
        
        # Check if the statement is of the form "X is Y"
        if words[1] == "is":
            # Add the rhyming relationship to the dictionary
            rhyming_dict[words[0]] = words[2]
            
        # Check if the statement is of the form "X not Y"
        elif words[1] == "not":
            # Add the rhyming relationship to the dictionary with the value "False"
            rhyming_dict[words[0]] = False
            
    # Iterate through the statements again
    for statement in statements:
        # Split the statement into words
        words = statement.split()
        
        # Check if the statement is of the form "X is Y"
        if words[1] == "is":
            # Check if the words are rhyming
            if rhyming_dict.get(words[0], False) == words[2]:
                return "wait what?"
            
    return "yes"

def main():
    # Read the number of statements
    n = int(input())
    
    # Read the statements
    statements = []
    for i in range(n):
        statements.append(input())
    
    # Check if the statements are consistent
    result = is_consistent(statements)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

