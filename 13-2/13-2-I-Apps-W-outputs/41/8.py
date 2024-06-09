
def get_min_days(n, m, d, a):
    # Initialize a dictionary to store the number of days needed to pass each subject
    days_needed = {}
    for i in range(m):
        days_needed[i+1] = a[i]

    # Initialize a set to store the passed subjects
    passed_subjects = set()

    # Initialize the minimum number of days needed to pass all subjects
    min_days = 0

    # Iterate through each day
    for i in range(n):
        # Check if the current day is allowed to pass an exam
        if d[i] != 0:
            # Check if the current subject has already been passed
            if d[i] not in passed_subjects:
                # Check if the current subject can be passed on the current day
                if days_needed[d[i]] > 0:
                    # Decrement the number of days needed to pass the current subject
                    days_needed[d[i]] -= 1

                    # Add the current subject to the set of passed subjects
                    passed_subjects.add(d[i])

                    # Increment the minimum number of days needed to pass all subjects
                    min_days += 1

    # Check if all subjects have been passed
    if len(passed_subjects) == m:
        return min_days
    else:
        return -1

