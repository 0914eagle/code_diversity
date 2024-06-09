
def solve(D, G, *args):
    p_scores = list(zip(*args))[0]
    c_scores = list(zip(*args))[1]

    # Initialize the minimum number of problems to solve
    min_problems = 0

    # Loop through each difficulty level
    for i in range(1, D+1):
        # Calculate the number of problems that can be solved at this difficulty level
        num_problems = p_scores[i-1]

        # Calculate the perfect bonus for solving all problems at this difficulty level
        perfect_bonus = c_scores[i-1]

        # Check if solving all problems at this difficulty level will give us a total score of G or more
        if num_problems * 100 * i + perfect_bonus >= G:
            # If it will, return the minimum number of problems needed to solve
            return min_problems + num_problems

        # Otherwise, increment the minimum number of problems to solve
        min_problems += num_problems

    # If we reach this point, it means that we need to solve all problems to achieve the objective
    return min_problems

