
def is_satisfiable(clauses):
    
    # Initialize a dictionary to store the current assignments of variables
    assignments = {}

    # Iterate through each clause in the instance
    for clause in clauses:
        # Initialize a flag to indicate whether the clause is satisfied
        satisfied = False

        # Iterate through each literal in the clause
        for literal in clause:
            # If the literal is positive (i.e., it has a plus sign), check if it is satisfied
            if literal > 0:
                # If the variable is not already assigned, assign it the value True
                if literal not in assignments:
                    assignments[literal] = True
                # If the variable is already assigned and its value is True, the clause is satisfied
                elif assignments[literal] == True:
                    satisfied = True
                    break
            # If the literal is negative (i.e., it has a minus sign), check if it is satisfied
            elif literal < 0:
                # If the variable is not already assigned, assign it the value False
                if literal not in assignments:
                    assignments[literal] = False
                # If the variable is already assigned and its value is False, the clause is satisfied
                elif assignments[literal] == False:
                    satisfied = True
                    break

        # If the clause is not satisfied, the instance is unsatisfiable
        if not satisfied:
            return False

    # If all clauses are satisfied, the instance is satisfiable
    return True

def is_satisfactory(m, n, clauses):
    
    # If the number of clauses is less than 8, the instance is unsatisfactory
    if m < 8:
        return "unsatisfactory"

    # Determine whether the instance is satisfiable
    if is_satisfiable(clauses):
        return "satisfactory"
    else:
        return "unsatisfactory"

if __name__ == '__main__':
    # Read the input from stdin
    m, n = map(int, input().split())
    clauses = [list(map(int, input().split())) for _ in range(m)]

    # Determine whether the instance is satisfactory
    result = is_satisfactory(m, n, clauses)

    # Print the result
    print(result)

