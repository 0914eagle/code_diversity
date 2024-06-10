
def is_satisfiable(clauses):
    # Initialize a dictionary to keep track of the values of the variables
    values = {}
    
    # Iterate over the clauses
    for clause in clauses:
        # Initialize a flag to indicate if the clause is satisfied
        satisfied = False
        
        # Iterate over the literals in the clause
        for literal in clause:
            # If the literal is positive, check if the variable is True
            if literal > 0:
                if literal in values and values[literal]:
                    satisfied = True
                    break
            # If the literal is negative, check if the variable is False
            elif literal < 0:
                if -literal in values and not values[-literal]:
                    satisfied = True
                    break
        
        # If the clause is not satisfied, return False
        if not satisfied:
            return False
    
    # If all clauses are satisfied, return True
    return True

def main():
    # Read the input data
    m, n = map(int, input().split())
    clauses = []
    for _ in range(m):
        clause = list(map(int, input().split()))
        clauses.append(clause)
    
    # Call the is_satisfiable function
    result = is_satisfiable(clauses)
    
    # Print the result
    if result:
        print("satisfactory")
    else:
        print("unsatisfactory")

if __name__ == '__main__':
    main()

