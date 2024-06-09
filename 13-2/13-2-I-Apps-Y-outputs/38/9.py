
def get_max_team_size(skills):
    # Sort the skills in non-decreasing order
    skills.sort()
    # Initialize the maximum team size and the current team size
    max_team_size = 0
    current_team_size = 0
    # Iterate through the skills
    for i in range(len(skills)):
        # If the current skill is within 5 of the previous skill, add it to the current team
        if i > 0 and skills[i] - skills[i-1] <= 5:
            current_team_size += 1
        # If the current skill is not within 5 of the previous skill, start a new team
        else:
            max_team_size = max(max_team_size, current_team_size)
            current_team_size = 1
    # Return the maximum team size
    return max(max_team_size, current_team_size)

