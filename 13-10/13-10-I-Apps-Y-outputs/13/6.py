
def is_correct_proof(proof):
    
    # Initialize a set to store all conclusions
    conclusions = set()
    
    # Loop through each line of the proof
    for line in proof:
        # Split the line into assumptions and conclusion
        assumptions, conclusion = line.split("->")
        
        # Remove any leading or trailing spaces
        assumptions = assumptions.strip()
        conclusion = conclusion.strip()
        
        # If the line has assumptions, check if they are all conclusions
        if assumptions:
            assumptions = assumptions.split()
            for assumption in assumptions:
                if assumption not in conclusions:
                    return False
        
        # Add the conclusion to the set of conclusions
        conclusions.add(conclusion)
    
    # If all lines are valid, return True
    return True

def get_error_line(proof):
    
    # Loop through each line of the proof
    for line_num, line in enumerate(proof, start=1):
        # Check if the line is valid
        if not is_correct_proof([line]):
            return line_num
    
    # If all lines are valid, return 0
    return 0

if __name__ == '__main__':
    # Read the input
    proof = [line.strip() for line in input().splitlines()]
    
    # Get the error line
    error_line = get_error_line(proof)
    
    # Print the output
    if error_line == 0:
        print("correct")
    else:
        print(error_line)

