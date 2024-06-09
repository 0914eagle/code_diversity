
def is_correct_proof(proof):
    # Initialize a set to store the conclusions of the previous lines
    previous_conclusions = set()
    
    # Iterate through the lines of the proof
    for line_number, line in enumerate(proof, start=1):
        # Split the line into assumptions, arrow, and conclusion
        assumptions, arrow, conclusion = line.split()
        
        # Check if the assumption is a conclusion of a previous line
        if assumptions not in previous_conclusions:
            return line_number
        
        # Add the conclusion to the set of previous conclusions
        previous_conclusions.add(conclusion)
    
    # If all lines are correct, return "correct"
    return "correct"

