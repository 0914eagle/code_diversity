
def solve(statements):
    # Initialize a dictionary to store the rhyming relationships
    rhyming_dict = {}

    # Iterate through the statements and populate the rhyming dictionary
    for statement in statements:
        words = statement.split()
        if len(words) == 3 and words[1] == "is":
            rhyming_dict[words[0]] = words[2]
        elif len(words) == 3 and words[1] == "not":
            rhyming_dict[words[0]] = None

    # Check if there are any contradictions in the rhyming dictionary
    for word, rhyme in rhyming_dict.items():
        if rhyme is not None and word != rhyme and rhyming_dict[rhyme] != word:
            return "wait what?"

    return "yes"

def main():
    # Read the number of statements
    num_statements = int(input())

    # Read the statements
    statements = []
    for _ in range(num_statements):
        statements.append(input())

    # Solve the problem
    result = solve(statements)

    # Print the result
    print(result)

if __name__ == '__main__':
    main()

