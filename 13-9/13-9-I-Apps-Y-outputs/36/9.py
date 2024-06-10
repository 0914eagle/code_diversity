
def check_satisfiability(instance):
    # Function to check if an instance of 3-SAT is satisfiable
    # instance: a list of clauses, each clause is a list of variables
    # Returns True if the instance is satisfiable, False otherwise
    
    # Initialize an assignment of variables
    assignment = {}
    
    # Iterate through each clause
    for clause in instance:
        # Initialize a flag to indicate if the clause is satisfied
        satisfied = False
        
        # Iterate through each literal in the clause
        for literal in clause:
            # If the literal is positive, check if the variable is True
            if literal > 0:
                if assignment.get(literal) == True:
                    satisfied = True
                    break
            # If the literal is negative, check if the variable is False
            else:
                if assignment.get(-literal) == False:
                    satisfied = True
                    break
        
        # If the clause is not satisfied, return False
        if not satisfied:
            return False
    
    # If all clauses are satisfied, return True
    return True

def check_judgement(instance):
    # Function to determine Øyvind's judgement on a 3-SAT instance
    # instance: a list of clauses, each clause is a list of variables
    # Returns "satisfactory" if the instance is satisfiable and has 8 or more clauses, "unsatisfactory" otherwise
    
    # Check if the instance is satisfiable
    if check_satisfiability(instance):
        # If the instance is satisfiable, check if it has 8 or more clauses
        if len(instance) >= 8:
            return "satisfactory"
        else:
            return "unsatisfactory"
    else:
        return "unsatisfactory"

if __name__ == '__main__':
    # Read the input instance from stdin
    instance = []
    for line in sys.stdin:
        instance.append(list(map(int, line.strip().split())))
    
    # Determine Øyvind's judgement on the instance
    judgement = check_judgement(instance)
    
    # Print the judgement to stdout
    print(judgement)

