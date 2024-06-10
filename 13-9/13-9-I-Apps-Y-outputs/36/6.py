
def is_satisfiable(clauses):
    # Initialize a dictionary to store the values of the variables
    variables = {}
    
    # Iterate over each clause
    for clause in clauses:
        # Initialize a flag to indicate whether the clause is satisfiable
        satisfiable = False
        
        # Iterate over each literal in the clause
        for literal in clause:
            # Check if the literal is positive or negative
            if literal > 0:
                # If the literal is positive, check if the variable is True
                if variables.get(literal, False):
                    # If the variable is True, the clause is satisfiable
                    satisfiable = True
                    break
            else:
                # If the literal is negative, check if the variable is False
                if variables.get(-literal, True):
                    # If the variable is False, the clause is satisfiable
                    satisfiable = True
                    break
        
        # If the clause is not satisfiable, return False
        if not satisfiable:
            return False
    
    # If all clauses are satisfiable, return True
    return True

def main():
    # Read the input
    m, n = map(int, input().split())
    clauses = []
    for _ in range(m):
        clauses.append(list(map(int, input().split())))
    
    # Check if the instance is satisfiable
    if is_satisfiable(clauses):
        print("satisfactory")
    else:
        print("unsatisfactory")

if __name__ == '__main__':
    main()

