
def is_correct(proof):
    # Initialize the set of axioms
    axioms = set(["ALICE", "BOB", "CARL"])
    
    # Iterate through the lines of the proof
    for i, line in enumerate(proof):
        # Split the line into assumptions and conclusion
        assumptions, conclusion = line.split(" -> ")
        
        # Check if the conclusion is an axiom
        if conclusion in axioms:
            continue
        
        # Check if all assumptions are conclusions of previous lines
        for assumption in assumptions.split():
            if assumption not in axioms and assumption not in conclusion:
                return i + 1
        
        # Add the conclusion to the set of axioms
        axioms.add(conclusion)
    
    # If all lines are correct, return "correct"
    return "correct"

def main():
    # Read the input
    n = int(input())
    proof = [input() for _ in range(n)]
    
    # Check if the proof is correct
    result = is_correct(proof)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

