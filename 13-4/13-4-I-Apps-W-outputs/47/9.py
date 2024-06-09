
def solve(n, m, k, timetable):
    # Initialize a variable to store the minimum number of hours spent in the university
    min_hours = float('inf')

    # Loop through all possible combinations of skipped lessons
    for skipped in range(0, k+1):
        # Initialize a variable to store the number of hours spent in the university for this combination
        hours = 0

        # Loop through each day
        for i in range(n):
            # If there are no lessons on this day, skip to the next day
            if not any(timetable[i]):
                continue

            # Find the first lesson that is not skipped
            first_lesson = next((j for j, lesson in enumerate(timetable[i], 1) if lesson and j not in skipped), None)

            # If there are no lessons that are not skipped, skip to the next day
            if first_lesson is None:
                continue

            # Find the last lesson that is not skipped
            last_lesson = next((j for j in range(first_lesson, m+1) if timetable[i][j-1] and j not in skipped), None)

            # Add the number of hours spent in the university for this day to the total
            hours += last_lesson - first_lesson + 1

        # If the number of hours spent in the university for this combination is less than the minimum, update the minimum
        if hours < min_hours:
            min_hours = hours

    # Return the minimum number of hours spent in the university
    return min_hours

