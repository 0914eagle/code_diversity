
def is_satisfiable(clauses, variables):
    # Check if the number of clauses is less than 8
    if len(clauses) < 8:
        return "unsatisfiable"
    
    # Check if the clause contains duplicates
    for clause in clauses:
        if len(set(clause)) != 3:
            return "unsatisfiable"
    
    # Check if the clause contains variables that are not in the range [-n, n]
    for clause in clauses:
        for variable in clause:
            if variable < -n or variable > n:
                return "unsatisfiable"
    
    # Check if the clause contains 0
    for clause in clauses:
        if 0 in clause:
            return "unsatisfiable"
    
    # If all checks pass, return "satisfiable"
    return "satisfiable"

def main():
    m, n = map(int, input().split())
    clauses = []
    for _ in range(m):
        clauses.append(list(map(int, input().split())))
    print(is_satisfiable(clauses, n))

if __name__ == '__main__':
    main()

