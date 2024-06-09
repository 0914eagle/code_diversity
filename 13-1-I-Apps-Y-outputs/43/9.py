
def form_team(n, k, a):
    # Sort the array in ascending order
    a.sort()
    # Initialize a set to store the indices of team members
    team = set()
    # Iterate through the array
    for i in range(n):
        # Check if the current element is already in the team
        if a[i] in team:
            # If it is, skip it
            continue
        # Add the current element to the team
        team.add(a[i])
        # Check if the team is complete
        if len(team) == k:
            # If it is, return the team
            return "YES\n" + " ".join(str(i + 1) for i in team)
    # If the team is not complete, return "NO"
    return "NO"

