
def is_valid_proof(proof):
    # Initialize a set to store the conclusions of the previous lines
    conclusions = set()
    
    # Iterate through the lines of the proof
    for line in proof:
        # Split the line into assumptions and conclusion
        assumptions, conclusion = line.split("->")
        
        # Remove any leading or trailing whitespace
        assumptions = assumptions.strip()
        conclusion = conclusion.strip()
        
        # If the conclusion is not in the set of conclusions, it is an axiom
        if conclusion not in conclusions:
            conclusions.add(conclusion)
        # If the conclusion is already in the set of conclusions, it is a repeated conclusion
        else:
            return False
        
        # Iterate through the assumptions and check if they are in the set of conclusions
        for assumption in assumptions.split():
            if assumption not in conclusions:
                return False
    
    # If all assumptions and conclusions are valid, return True
    return True

def main():
    # Read the number of lines in the proof
    n = int(input())
    
    # Read the lines of the proof
    proof = []
    for i in range(n):
        line = input()
        proof.append(line)
    
    # Check if the proof is valid
    if is_valid_proof(proof):
        print("correct")
    else:
        print(f"Line {i+1} is incorrect")

if __name__ == '__main__':
    main()

