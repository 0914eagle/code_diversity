
def check_proof(proof):
    
    assumptions = set()
    for line in proof:
        if line.startswith("->"):
            # If the line is an assumption, add it to the set of assumptions
            assumptions.add(line.strip("-> "))
        else:
            # If the line is a conclusion, check if it is an assumption
            if line.strip("-> ") not in assumptions:
                return "incorrect"
    return "correct"

def get_error_line(proof):
    
    for i, line in enumerate(proof, start=1):
        if check_proof(line) == "incorrect":
            return i
    return None

def main():
    num_lines = int(input())
    proof = []
    for _ in range(num_lines):
        proof.append(input())
    print(get_error_line(proof))

if __name__ == '__main__':
    main()

