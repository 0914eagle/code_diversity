
def solve(n, p):
    # Initialize a dictionary to store the number of holes in each badge
    holes = {i: 0 for i in range(1, n + 1)}
    
    # Iterate through the list of reported students
    for i in range(n):
        # If the current student has already received a hole in his badge, skip him
        if holes[i] == 1:
            continue
        # If the current student has not received a hole in his badge, find the next student in the list who has already received a hole in his badge
        while holes[p[i]] == 0:
            p[i] = p[p[i]]
        # Update the number of holes in the current student's badge
        holes[i] = 1
    
    # Return the student with two holes in his badge
    return [holes[i] for i in range(1, n + 1)]

