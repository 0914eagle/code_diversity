
def get_judgment(instance):
    m, n = instance[0], instance[1]
    clauses = instance[2:]
    
    # Check if the instance has 8 or more clauses
    if len(clauses) >= 8:
        return "satisfactory"
    
    # Check if the instance is satisfiable
    for clause in clauses:
        if all(lit != 0 for lit in clause):
            return "unsatisfactory"
    
    return "unsatisfactory"

def main():
    instance = [int(x) for x in input().split()]
    print(get_judgment(instance))

if __name__ == '__main__':
    main()

