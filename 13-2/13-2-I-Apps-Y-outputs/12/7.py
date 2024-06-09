
def is_valid_proof(proof):
    # Initialize a dictionary to store the assumptions and conclusions
    assumptions = {}
    
    # Iterate through the lines of the proof
    for line in proof:
        # Split the line into assumptions, arrow, and conclusion
        assumptions, arrow, conclusion = line.split()
        
        # Check if the conclusion is already in the dictionary
        if conclusion in assumptions:
            return False
        
        # Add the assumption and conclusion to the dictionary
        assumptions[conclusion] = assumptions
    
    # If all lines are valid, return True
    return True

