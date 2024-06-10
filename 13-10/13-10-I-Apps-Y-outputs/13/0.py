
def is_valid_assumption(assumptions, conclusion):
    return conclusion in assumptions

def is_valid_proof(proof):
    assumptions = set()
    for line in proof:
        assumptions.update(line[0])
        if not is_valid_assumption(assumptions, line[2]):
            return False
    return True

def get_first_error(proof):
    for i, line in enumerate(proof, 1):
        if not is_valid_assumption(line[0], line[2]):
            return i
    return None

def main():
    n = int(input())
    proof = [input().split() for _ in range(n)]
    if is_valid_proof(proof):
        print("correct")
    else:
        print(get_first_error(proof))

if __name__ == '__main__':
    main()

