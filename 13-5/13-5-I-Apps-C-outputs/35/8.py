
def get_character_type(statement):
    # Function to get the character type of a candidate
    # based on the statement they uttered
    if "truther" in statement:
        return "truther"
    elif "fabulist" in statement:
        return "fabulist"
    elif "charlatan" in statement:
        return "charlatan"
    else:
        return "unknown"

def get_candidate_types(candidates, statements):
    # Function to get the character type of each candidate
    # based on the statements they uttered
    candidate_types = {}
    for candidate in candidates:
        candidate_types[candidate] = "unknown"
    for statement in statements:
        candidate, statement = statement.split(" ")
        candidate = int(candidate)
        character_type = get_character_type(statement)
        if candidate_types[candidate] == "unknown":
            candidate_types[candidate] = character_type
        elif candidate_types[candidate] != character_type:
            candidate_types[candidate] = "unknown"
    return candidate_types

def main():
    # Main function to read input, process it, and print output
    N, K = map(int, input().split())
    candidates = list(range(1, N+1))
    statements = []
    for _ in range(K):
        statement = input()
        statements.append(statement)
    candidate_types = get_candidate_types(candidates, statements)
    for candidate in candidates:
        print(candidate_types[candidate])

if __name__ == '__main__':
    main()

