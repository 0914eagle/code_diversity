
def get_character_type(statement):
    # Function to get the character type of a candidate based on their statement
    # The statement is a string containing the proposition and the name of the candidate
    # The function returns the character type of the candidate as a string
    proposition, candidate = statement.split()
    if proposition == "truther":
        return "truther"
    elif proposition == "fabulist":
        return "fabulist"
    elif proposition == "charlatan":
        return "charlatan"
    elif proposition == "not":
        return "not"
    elif proposition == "and":
        return "and"
    elif proposition == "xor":
        return "xor"
    else:
        return "unknown"

def get_candidate_types(candidates, statements):
    # Function to get the character types of all candidates based on their statements
    # The candidates is a list of strings containing the names of the candidates
    # The statements is a list of strings containing the propositions and the names of the candidates
    # The function returns a dictionary with the character types of all candidates
    candidate_types = {}
    for candidate in candidates:
        candidate_types[candidate] = "unknown"
    for statement in statements:
        proposition, candidate = statement.split()
        if proposition == "truther":
            candidate_types[candidate] = "truther"
        elif proposition == "fabulist":
            candidate_types[candidate] = "fabulist"
        elif proposition == "charlatan":
            candidate_types[candidate] = "charlatan"
        elif proposition == "not":
            candidate_types[candidate] = "not"
        elif proposition == "and":
            candidate_types[candidate] = "and"
        elif proposition == "xor":
            candidate_types[candidate] = "xor"
    return candidate_types

def main():
    # Main function to read the input, process the data, and print the output
    # The input is a list of strings containing the names of the candidates and the propositions and the names of the candidates
    # The output is a list of strings containing the character types of the candidates
    candidates = input().split()
    statements = input().split()
    candidate_types = get_candidate_types(candidates, statements)
    for candidate in candidates:
        print(candidate_types[candidate])

if __name__ == '__main__':
    main()

