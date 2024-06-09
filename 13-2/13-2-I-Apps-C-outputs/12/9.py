
def find_best_subsequence(k, answers):
    # Initialize variables
    best_subsequence = []
    best_success_rate = 0
    current_subsequence = []
    current_success_rate = 0
    
    # Iterate through the answers
    for answer in answers:
        # If the answer is correct, add it to the current subsequence
        if answer == 1:
            current_subsequence.append(answer)
            current_success_rate += 1
        # If the answer is incorrect, add it to the current subsequence and check if it is a better subsequence
        else:
            current_subsequence.append(answer)
            current_success_rate += 1
            if len(current_subsequence) >= k and current_success_rate > best_success_rate:
                best_subsequence = current_subsequence
                best_success_rate = current_success_rate
            current_subsequence = []
            current_success_rate = 0
    
    # If there are any remaining answers in the current subsequence, check if it is a better subsequence
    if len(current_subsequence) >= k and current_success_rate > best_success_rate:
        best_subsequence = current_subsequence
        best_success_rate = current_success_rate
    
    # Return the index and length of the best subsequence
    return (best_subsequence[0], len(best_subsequence))

