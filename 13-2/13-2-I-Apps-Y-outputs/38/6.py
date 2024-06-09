
def get_max_team_size(a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the maximum team size and the current team size
    max_team_size = 0
    curr_team_size = 0
    # Iterate through the array
    for i in range(len(a)):
        # If the current team size is 0, add the current student to the team
        if curr_team_size == 0:
            curr_team_size += 1
        # If the current team size is not 0, check if the current student's skill is within 5 of the previous student's skill
        else:
            if abs(a[i] - a[i-1]) <= 5:
                curr_team_size += 1
            else:
                # If the current student's skill is not within 5 of the previous student's skill, update the maximum team size
                max_team_size = max(max_team_size, curr_team_size)
                curr_team_size = 1
    # Add the last student to the team
    max_team_size = max(max_team_size, curr_team_size+1)
    return max_team_size

