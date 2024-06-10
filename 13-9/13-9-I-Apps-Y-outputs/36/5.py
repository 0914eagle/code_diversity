
def is_satisfiable(clauses):
    variables = set()
    for clause in clauses:
        variables.update(clause)
    variables = list(variables)
    variables.sort()
    assignment = [False] * len(variables)
    return is_satisfiable_helper(clauses, variables, assignment)

def is_satisfiable_helper(clauses, variables, assignment):
    if not clauses:
        return True
    clause = clauses.pop()
    for i in range(len(variables)):
        if assignment[i] == False and is_satisfiable_helper(clauses, variables, assignment[:i] + [True] + assignment[i+1:]):
            return True
        if assignment[i] == True and is_satisfiable_helper(clauses, variables, assignment[:i] + [False] + assignment[i+1:]):
            return True
    return False

def get_judgement(clauses):
    if len(clauses) < 8:
        return "unsatisfactory"
    else:
        return "satisfactory"

def main():
    m, n = map(int, input().split())
    clauses = []
    for _ in range(m):
        clauses.append(set(map(int, input().split())))
    print(get_judgement(clauses))

if __name__ == '__main__':
    main()

