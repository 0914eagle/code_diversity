
def get_input():
    N = int(input())
    statements = []
    for i in range(N):
        statements.append(input())
    return statements

def check_consistency(statements):
    # Initialize a dictionary to store the relationships between words
    relationships = {}
    for statement in statements:
        # Split the statement into two words
        words = statement.split()
        # Check if the words are already in the dictionary
        if words[0] in relationships and words[1] in relationships[words[0]]:
            # If both words are already in the dictionary and they are not equal, return "wait what?"
            return "wait what?"
        # Add the words to the dictionary with their relationship
        if words[0] not in relationships:
            relationships[words[0]] = {words[1]}
        else:
            relationships[words[0]].add(words[1])
        if words[1] not in relationships:
            relationships[words[1]] = {words[0]}
        else:
            relationships[words[1]].add(words[0])
    
    # Check if all the words are consistent with each other
    for word in relationships:
        if len(relationships[word]) != 1:
            # If a word has more than one relationship, return "wait what?"
            return "wait what?"
    
    # If all the words are consistent with each other, return "yes"
    return "yes"

def main():
    statements = get_input()
    print(check_consistency(statements))

if __name__ == '__main__':
    main()

