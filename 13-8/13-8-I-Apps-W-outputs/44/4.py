
def find_badge_holes(n, p):
    # Initialize a dictionary to store the number of holes for each student
    holes = {i: 0 for i in range(1, n + 1)}
    
    # Iterate through the list of reported students
    for i in range(n):
        # If the student has already received a hole in his badge, skip it
        if holes[i] == 1:
            continue
        # If the student has reported another student, add a hole to that student's badge
        holes[p[i]] += 1
    
    # Return a list of students with two holes in their badges
    return [i for i in range(1, n + 1) if holes[i] == 2]

