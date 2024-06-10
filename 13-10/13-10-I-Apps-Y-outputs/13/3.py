
def check_proof(proof):
    # Initialize a set to store the conclusions
    conclusions = set()
    
    # Iterate over the lines of the proof
    for line in proof:
        # Split the line into assumptions and conclusion
        assumptions, conclusion = line.split("->")
        
        # Remove any leading or trailing spaces
        assumptions = assumptions.strip()
        conclusion = conclusion.strip()
        
        # Check if the conclusion is already in the set of conclusions
        if conclusion in conclusions:
            return "incorrect"
        
        # Add the conclusion to the set of conclusions
        conclusions.add(conclusion)
        
        # Check if the assumptions are all in the set of conclusions
        for assumption in assumptions.split():
            if assumption not in conclusions:
                return "incorrect"
    
    # If all assumptions and conclusions are valid, return "correct"
    return "correct"

def main():
    # Read the number of lines in the proof
    num_lines = int(input())
    
    # Read the proof
    proof = []
    for _ in range(num_lines):
        proof.append(input())
    
    # Check the proof
    result = check_proof(proof)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

