
def get_min_hours(n, m, k, timetable):
    # Initialize variables
    hours_spent = 0
    skipped_lessons = 0

    # Iterate over each day
    for day in timetable:
        # Get the number of lessons for the current day
        num_lessons = day.count("1")

        # Check if the number of lessons is greater than the allowed number of skipped lessons
        if num_lessons > k:
            return -1

        # Iterate over each hour in the day
        for hour in range(m):
            # Check if there is a lesson at the current hour
            if day[hour] == "1":
                # Increment the number of hours spent in the university
                hours_spent += 1
            else:
                # Check if the current hour is the first hour with no lesson
                if skipped_lessons == 0:
                    # Set the first hour with no lesson as the start hour
                    start_hour = hour

                # Increment the number of skipped lessons
                skipped_lessons += 1

        # Check if the current day has no lessons
        if skipped_lessons == m:
            # Do not spend any hours in the university on this day
            hours_spent += 0
        else:
            # Spend the difference between the number of skipped lessons and the allowed number of skipped lessons in the university
            hours_spent += k - skipped_lessons

        # Reset the number of skipped lessons for the next day
        skipped_lessons = 0

    return hours_spent

