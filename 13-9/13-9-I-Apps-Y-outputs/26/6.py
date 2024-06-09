
def solve(n, skills):
    # Sort the skills in non-decreasing order
    skills.sort()
    # Initialize the minimum number of problems to 0
    min_problems = 0
    # Iterate through the skills and form teams
    for i in range(0, n, 2):
        # If the skills are not equal, increase the minimum number of problems
        if skills[i] != skills[i+1]:
            min_problems += abs(skills[i] - skills[i+1])
    return min_problems

