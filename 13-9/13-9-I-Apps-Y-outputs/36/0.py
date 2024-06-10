
def is_satisfiable(clauses, n):
    # Initialize an array to store the values of the variables
    values = [None] * n
    
    # Iterate over the clauses
    for clause in clauses:
        # Check if the clause is satisfiable
        if all(values[abs(literal) - 1] != literal < 0 for literal in clause):
            # If the clause is not satisfiable, return False
            return False
    
    # If all clauses are satisfiable, return True
    return True

def judge_instance(instance):
    # Get the number of clauses and variables from the instance
    m, n = map(int, instance.split())
    
    # Get the clauses from the instance
    clauses = [tuple(map(int, instance.split())) for _ in range(m)]
    
    # Check if the instance is satisfiable
    if is_satisfiable(clauses, n):
        return "satisfactory"
    else:
        return "unsatisfactory"

if __name__ == '__main__':
    # Get the input instance
    instance = input()
    
    # Judge the instance
    print(judge_instance(instance))

