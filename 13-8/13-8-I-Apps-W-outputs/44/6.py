
def find_badge_student(n, p):
    # Initialize a dictionary to store the number of holes in each badge
    badge_holes = {i: 0 for i in range(1, n + 1)}

    # Iterate through the list of reported students
    for i in range(n):
        # Get the current student and the student who reported him
        current_student = i + 1
        reported_student = p[i]

        # If the current student has already received a hole in his badge, skip him
        if badge_holes[current_student] == 1:
            continue

        # If the current student reported someone, add a hole to his badge
        if reported_student != 0:
            badge_holes[current_student] += 1

        # If the reported student has already received a hole in his badge, add a hole to the current student's badge
        if badge_holes[reported_student] == 1:
            badge_holes[current_student] += 1

    # Find the student with two holes in his badge
    two_hole_student = [k for k, v in badge_holes.items() if v == 2]

    return two_hole_student[0]

