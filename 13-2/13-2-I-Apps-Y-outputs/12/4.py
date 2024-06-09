
def is_valid_proof(proof):
    # Initialize a dictionary to store the assumptions and conclusions
    assumptions = {}
    
    # Iterate through the lines of the proof
    for line in proof:
        # Split the line into assumptions, arrow, and conclusion
        assumptions, arrow, conclusion = line.split()
        
        # Check if the conclusion is already in the dictionary
        if conclusion in assumptions:
            # If it is, return the line number
            return line_number
    
    # If we reach this point, all lines are valid
    return "correct"

