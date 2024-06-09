
def is_proof_correct(proof):
    # Initialize a dictionary to store the assumptions and conclusions
    assumptions = {}
    
    # Iterate through the lines of the proof
    for line_num, line in enumerate(proof, start=1):
        # Split the line into assumptions, arrow, and conclusion
        assumptions, _, conclusion = line.split()
        
        # Check if the conclusion is already in the dictionary
        if conclusion in assumptions:
            return line_num
        
        # Add the assumption and conclusion to the dictionary
        assumptions[assumption] = conclusion
    
    # If all lines are correct, return "correct"
    return "correct"

