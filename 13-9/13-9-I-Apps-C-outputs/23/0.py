
def solve(statements):
    # Initialize a dictionary to store the relationships between words
    relationships = {}
    
    # Iterate over the statements
    for statement in statements:
        # Split the statement into words
        words = statement.split()
        
        # Check if the statement is in the form "X is Y"
        if words[1] == "is":
            # Add the relationship to the dictionary
            relationships[words[0]] = words[2]
    
    # Iterate over the statements again
    for statement in statements:
        # Split the statement into words
        words = statement.split()
        
        # Check if the statement is in the form "X not Y"
        if words[1] == "not":
            # Check if the relationship between X and Y already exists
            if words[0] in relationships and relationships[words[0]] == words[2]:
                # If the relationship exists, return "wait what?"
                return "wait what?"
    
    # If all statements are consistent, return "yes"
    return "yes"

def main():
    # Read the number of statements
    num_statements = int(input())
    
    # Read the statements
    statements = []
    for i in range(num_statements):
        statements.append(input())
    
    # Solve the problem
    result = solve(statements)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

