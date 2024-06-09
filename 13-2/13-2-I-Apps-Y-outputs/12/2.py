
def is_correct_proof(proof):
    # Initialize a dictionary to store the assumptions and conclusions
    assumptions = {}
    conclusions = {}
    
    # Iterate through the lines of the proof
    for line_num, line in enumerate(proof, start=1):
        # Split the line into assumptions, arrow, and conclusion
        assumptions, arrow, conclusion = line.split()
        
        # Check if the assumption is a valid conclusion from a previous line
        if assumptions not in conclusions:
            return line_num
        
        # Add the assumption and conclusion to the dictionaries
        assumptions[assumptions] = conclusion
        conclusions[conclusion] = assumptions
    
    # If all lines are correct, return "correct"
    return "correct"

