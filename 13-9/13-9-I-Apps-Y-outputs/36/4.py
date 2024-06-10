
def is_satisfiable(clauses):
    # Initialize a dictionary to store the values of the variables
    variables = {}
    for clause in clauses:
        # Check if the clause is satisfied
        satisfied = True
        for literal in clause:
            # If the literal is negative, check if the variable is False
            if literal < 0:
                variable = abs(literal)
                if variable not in variables or variables[variable] == True:
                    satisfied = False
                    break
            # If the literal is positive, check if the variable is True
            else:
                variable = literal
                if variable not in variables or variables[variable] == False:
                    satisfied = False
                    break
        # If the clause is not satisfied, assign a value to the variable
        if not satisfied:
            variable = abs(clause[0])
            if variable not in variables:
                variables[variable] = True
            else:
                variables[variable] = not variables[variable]
    # Check if all clauses are satisfied
    for clause in clauses:
        satisfied = True
        for literal in clause:
            # If the literal is negative, check if the variable is False
            if literal < 0:
                variable = abs(literal)
                if variable not in variables or variables[variable] == True:
                    satisfied = False
                    break
            # If the literal is positive, check if the variable is True
            else:
                variable = literal
                if variable not in variables or variables[variable] == False:
                    satisfied = False
                    break
        if not satisfied:
            return "unsatisfiable"
    return "satisfiable"

def main():
    m, n = map(int, input().split())
    clauses = []
    for _ in range(m):
        clause = tuple(map(int, input().split()))
        clauses.append(clause)
    print(is_satisfiable(clauses))

if __name__ == '__main__':
    main()

