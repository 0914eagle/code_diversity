
def is_valid_proof(proof):
    # Initialize a dictionary to store the assumptions and conclusions
    assumptions = {}
    conclusions = {}
    
    # Iterate over the lines of the proof
    for line_num, line in enumerate(proof, start=1):
        # Split the line into assumptions, arrow, and conclusion
        assumptions_str, arrow, conclusion = line.split()
        
        # Check if the arrow is correct
        if arrow != "->":
            return line_num
        
        # Check if the conclusion is already a conclusion
        if conclusion in conclusions:
            return line_num
        
        # Add the assumption and conclusion to the dictionaries
        if assumptions_str:
            for assumption in assumptions_str.split():
                assumptions[assumption] = line_num
        conclusions[conclusion] = line_num
    
    # Check if all assumptions are conclusions of previous lines
    for assumption, line_num in assumptions.items():
        if line_num not in conclusions.values():
            return line_num
    
    # If all checks pass, the proof is valid
    return "correct"

def main():
    n = int(input())
    proof = []
    for _ in range(n):
        proof.append(input())
    print(is_valid_proof(proof))

if __name__ == '__main__':
    main()

