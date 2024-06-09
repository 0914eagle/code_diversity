
def is_proof_correct(proof):
    # Initialize a set to store the conclusions of the previous lines
    conclusions = set()
    
    # Iterate through the lines of the proof
    for line_num, line in enumerate(proof, start=1):
        # Split the line into assumptions, arrow, and conclusion
        assumptions, arrow, conclusion = line.split()
        
        # Check if the conclusion has already been derived
        if conclusion in conclusions:
            return line_num
        
        # Check if the assumptions are all conclusions of previous lines
        for assumption in assumptions.split():
            if assumption not in conclusions:
                return line_num
        
        # Add the conclusion to the set of conclusions
        conclusions.add(conclusion)
    
    # If all lines are correct, return "correct"
    return "correct"

