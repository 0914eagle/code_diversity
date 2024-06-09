
def solve(n, m, k, timetable):
    # Initialize a variable to store the minimum number of hours spent in the university
    min_hours = 0
    # Iterate over each day in the week
    for i in range(n):
        # Initialize a variable to store the number of lessons skipped in the current day
        skipped_lessons = 0
        # Iterate over each hour in the day
        for j in range(m):
            # Check if there is a lesson at the current hour
            if timetable[i][j] == "1":
                # If the current hour has a lesson and Ivan has not skipped enough lessons, skip the lesson
                if skipped_lessons < k:
                    skipped_lessons += 1
                # Otherwise, attend the lesson and increment the minimum number of hours spent in the university
                else:
                    min_hours += 1
        # If Ivan skipped all lessons in the current day, he doesn't go to the university that day
        if skipped_lessons == m:
            min_hours += 0
    # Return the minimum number of hours spent in the university
    return min_hours

