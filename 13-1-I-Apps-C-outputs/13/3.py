
def solve(n, t, grade):
    # Initialize the maximum grade to be the initial grade
    max_grade = grade
    # Loop through each second
    for i in range(t):
        # Get the current grade
        current_grade = max_grade
        # Round the grade to the nearest integer
        rounded_grade = round(current_grade)
        # Check if the rounded grade is greater than the current grade
        if rounded_grade > current_grade:
            # Update the maximum grade
            max_grade = rounded_grade
        # Round the grade to the nearest tenth
        rounded_grade = round(current_grade, 1)
        # Check if the rounded grade is greater than the current grade
        if rounded_grade > current_grade:
            # Update the maximum grade
            max_grade = rounded_grade
    # Return the maximum grade
    return max_grade

