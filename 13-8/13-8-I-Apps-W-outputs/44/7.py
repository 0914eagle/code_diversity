
def find_badge_holder(n, p):
    # Initialize a dictionary to store the number of holes in each badge
    badge_holes = {}
    for i in range(1, n+1):
        badge_holes[i] = 0
    
    # Iterate through the list of reported students
    for i in range(n):
        # If the current student has already been reported, skip them
        if badge_holes[i] == 1:
            continue
        # Find the next student in the sequence according to the list of reported students
        next_student = p[i-1]
        # Add a hole to the badge of the next student
        badge_holes[next_student] += 1
        # If the next student has already been reported, add a hole to their badge as well
        if badge_holes[next_student] == 1:
            badge_holes[p[next_student-1]] += 1
    
    # Find the student with two holes in their badge
    for i in range(1, n+1):
        if badge_holes[i] == 2:
            return i

