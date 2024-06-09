
def solve(routines):
    # Initialize a dictionary to keep track of the dancers and their quick change status
    dancers = {}
    for routine in routines:
        for dancer in routine:
            if dancer not in dancers:
                dancers[dancer] = "normal"
            elif dancers[dancer] == "quick":
                dancers[dancer] = "normal"
    
    # Count the number of quick changes required
    quick_changes = 0
    for i in range(len(routines) - 1):
        routine1 = routines[i]
        routine2 = routines[i + 1]
        for dancer in routine1:
            if dancer in routine2 and dancers[dancer] == "normal":
                quick_changes += 1
                dancers[dancer] = "quick"
    
    return quick_changes

