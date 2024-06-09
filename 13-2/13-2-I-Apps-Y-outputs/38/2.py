
def get_max_team_size(skills):
    # Sort the skills in non-decreasing order
    skills.sort()
    # Initialize the maximum team size and the current team size
    max_team_size = 0
    curr_team_size = 0
    # Iterate through the skills and check if they are balanced
    for i in range(len(skills)):
        if curr_team_size == 0 or abs(skills[i] - skills[i - 1]) <= 5:
            curr_team_size += 1
        else:
            max_team_size = max(max_team_size, curr_team_size)
            curr_team_size = 1
    # Return the maximum team size
    return max(max_team_size, curr_team_size)

