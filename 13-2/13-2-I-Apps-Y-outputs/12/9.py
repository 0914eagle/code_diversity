
def is_correct_proof(proof):
    # Initialize a dictionary to store the assumptions and conclusions
    assumptions = {}
    conclusions = {}
    
    # Iterate through the proof lines
    for line_num, line in enumerate(proof, start=1):
        # Split the line into assumptions, arrow, and conclusion
        assumptions_str, arrow, conclusion_str = line.split()
        assumptions = assumptions_str.split(" ")
        conclusion = conclusion_str
        
        # Check if the conclusion is already in the dictionary of conclusions
        if conclusion in conclusions:
            return line_num
        
        # Check if all assumptions are in the dictionary of conclusions
        for assumption in assumptions:
            if assumption not in conclusions:
                return line_num
        
        # Add the conclusion to the dictionary of conclusions
        conclusions[conclusion] = True
    
    # If all lines are correct, return "correct"
    return "correct"

