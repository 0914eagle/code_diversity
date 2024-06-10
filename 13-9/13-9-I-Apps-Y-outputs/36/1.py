
def is_satisfiable(clauses):
    # Initialize a dictionary to store the values of the variables
    variables = {}
    # Iterate over the clauses
    for clause in clauses:
        # Initialize a flag to indicate if the clause is satisfiable
        satisfiable = True
        # Iterate over the literals in the clause
        for literal in clause:
            # Check if the literal is positive or negative
            if literal > 0:
                # If the literal is positive, check if the variable is True
                if variables.get(literal, False) == False:
                    # If the variable is False, the clause is not satisfiable
                    satisfiable = False
                    break
            else:
                # If the literal is negative, check if the variable is False
                if variables.get(-literal, True) == True:
                    # If the variable is True, the clause is not satisfiable
                    satisfiable = False
                    break
        # If the clause is satisfiable, set the variable values
        if satisfiable:
            for literal in clause:
                if literal > 0:
                    variables[literal] = True
                else:
                    variables[-literal] = False
    # Check if the instance is satisfiable
    if len(variables) == len(clauses):
        return "satisfactory"
    else:
        return "unsatisfactory"

def main():
    # Read the input data
    m, n = map(int, input().split())
    clauses = []
    for _ in range(m):
        clauses.append(list(map(int, input().split())))
    # Call the is_satisfiable function
    print(is_satisfiable(clauses))

if __name__ == '__main__':
    main()

