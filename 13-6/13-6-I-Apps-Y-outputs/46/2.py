
def solve(D, G, *args):
    p_scores = list(zip(*args))[0]
    c_bonuses = list(zip(*args))[1]

    # Initialize the minimum number of problems to solve as the highest possible score
    min_problems = sum(p_scores)

    # Iterate through each possible number of problems to solve
    for num_problems in range(1, D + 1):
        # Initialize the current score as the base score
        current_score = sum(p_scores[:num_problems])

        # Add the perfect bonus for each group of problems with the same score
        for i in range(1, D + 1):
            num_problems_with_score = p_scores.count(100 * i)
            if num_problems_with_score > 0:
                current_score += c_bonuses[i - 1]

        # If the current score is greater than or equal to the goal, update the minimum number of problems to solve
        if current_score >= G:
            min_problems = min(min_problems, num_problems)

    return min_problems

