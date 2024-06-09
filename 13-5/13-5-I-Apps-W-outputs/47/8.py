
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
    for routine in routines:
        for i in range(len(routine) - 1):
            if routine[i] not in dancers or routine[i + 1] not in dancers:
                continue
            if dancers[routine[i]] == "normal" and dancers[routine[i + 1]] == "normal":
                dancers[routine[i]] = "quick"
                dancers[routine[i + 1]] = "quick"
                quick_changes += 1
    
    return quick_changes

