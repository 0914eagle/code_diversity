
def solve(D, G, p_c_list):
    # Initialize variables
    total_score = 0
    problems_solved = 0

    # Sort the list of problems by score in descending order
    p_c_list.sort(key=lambda x: x[0], reverse=True)

    # Loop through the list of problems
    for p, c in p_c_list:
        # Check if solving this problem will give us a total score of G or more
        if total_score + p >= G:
            # If so, break out of the loop
            break
        # Otherwise, solve the problem and update the total score
        total_score += p
        problems_solved += 1

    # Return the number of problems solved
    return problems_solved

