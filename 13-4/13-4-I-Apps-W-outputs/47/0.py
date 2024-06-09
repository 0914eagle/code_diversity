
def solve(n, m, k, timetable):
    # Initialize variables
    hours_spent = 0
    skipped_lessons = 0

    # Iterate over each day
    for day in timetable:
        # Check if there are any lessons on this day
        if day.count("1") > 0:
            # Find the first and last lesson on this day
            first_lesson = day.index("1")
            last_lesson = day.rindex("1")

            # Calculate the number of hours spent on this day
            hours_spent += last_lesson - first_lesson + 1

            # Check if the number of skipped lessons is less than or equal to k
            if skipped_lessons <= k:
                # Skip the first lesson on this day
                skipped_lessons += 1
            else:
                # Attend all lessons on this day
                hours_spent += m - 1
        else:
            # There are no lessons on this day, so spend 0 hours
            hours_spent += 0

    # Return the minimum number of hours spent in the university
    return hours_spent

