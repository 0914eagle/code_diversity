
def is_proof_correct(proof):
    
    # Initialize the set of assumptions
    assumptions = set()
    
    # Loop through each line of the proof
    for line in proof:
        # Split the line into assumptions and conclusion
        assumptions, conclusion = line.split(" -> ")
        
        # Check if the conclusion is already an assumption
        if conclusion in assumptions:
            return False
        
        # Add the conclusion to the set of assumptions
        assumptions.add(conclusion)
    
    # Check if all assumptions were used
    if len(assumptions) != len(set(assumptions)):
        return False
    
    # If all assumptions were used and no assumption is the conclusion, the proof is correct
    return True

def main():
    # Read the number of lines in the proof
    n = int(input())
    
    # Read the proof
    proof = []
    for _ in range(n):
        proof.append(input())
    
    # Check if the proof is correct
    if is_proof_correct(proof):
        print("correct")
    else:
        print("incorrect")

if __name__ == '__main__':
    main()

