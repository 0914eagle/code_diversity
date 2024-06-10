
def is_valid_proof(proof):
    
    assumptions = set()
    for line in proof:
        if "->" in line:
            assumptions.add(line.split("->")[0].strip())
        if line.split("->")[1].strip() in assumptions:
            return False
    return True

def get_first_error(proof):
    
    for i, line in enumerate(proof, start=1):
        if not is_valid_proof([line]):
            return i
    return 0

def main():
    n = int(input())
    proof = []
    for _ in range(n):
        proof.append(input())
    if get_first_error(proof) == 0:
        print("correct")
    else:
        print(get_first_error(proof))

if __name__ == '__main__':
    main()

