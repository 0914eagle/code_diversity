
def solve(n, c, t):
    # Initialize a list to store the answers
    answers = [False] * n
    
    # Set the first answer to be True
    answers[0] = True
    
    # Iterate through the list of charges
    for i in range(1, n):
        # Check if the current answer is True
        if answers[i]:
            # If the current answer is True, check if the previous answer is True
            if answers[i-1]:
                # If the previous answer is True, set the current answer to be True
                answers[i] = True
            # If the previous answer is False, set the current answer to be False
            else:
                answers[i] = False
        # If the current answer is False, check if the previous answer is True
        else:
            # If the previous answer is True, set the current answer to be False
            if answers[i-1]:
                answers[i] = False
            # If the previous answer is False, set the current answer to be False
            else:
                answers[i] = False
    
    # Return True if all answers are True, False otherwise
    return all(answers)

