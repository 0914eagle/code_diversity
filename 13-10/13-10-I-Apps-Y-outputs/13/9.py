
def is_correct(proof):
    # Initialize a dictionary to store the assumptions and conclusions
    assumptions = {}
    
    # Iterate over the lines of the proof
    for line in proof:
        # Split the line into assumptions, arrow, and conclusion
        assumptions, arrow, conclusion = line.split()
        
        # Check if the arrow is valid
        if arrow != "->":
            return False
        
        # Check if the conclusion is already in the dictionary
        if conclusion in assumptions:
            return False
        
        # Add the assumption and conclusion to the dictionary
        assumptions[conclusion] = assumptions
    
    # Check if all assumptions have been used
    for assumption in assumptions:
        if assumption not in conclusions:
            return False
    
    # If all lines are correct, return "correct"
    return "correct"

def main():
    # Read the number of lines in the proof
    n = int(input())
    
    # Read the proof
    proof = []
    for i in range(n):
        proof.append(input())
    
    # Check if the proof is correct
    result = is_correct(proof)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

