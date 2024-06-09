
def solve(n, m, d, a):
    # Initialize a dictionary to store the number of days needed to pass each subject
    days_needed = {}
    for i in range(m):
        days_needed[i+1] = a[i]

    # Initialize a set to store the passed subjects
    passed_subjects = set()

    # Initialize the number of days spent preparing
    days_spent = 0

    # Iterate through each day
    for i in range(n):
        # Check if the current day is allowed to pass an exam
        if d[i] != 0:
            # Check if the current subject has already been passed
            if d[i] not in passed_subjects:
                # Check if the current day has enough time to pass the current subject
                if days_needed[d[i]] <= days_spent:
                    # Pass the current subject and update the number of days spent
                    passed_subjects.add(d[i])
                    days_spent = 0
                else:
                    # Not enough time to pass the current subject, return -1
                    return -1
        # Increment the number of days spent preparing
        days_spent += 1

    # Check if all subjects have been passed
    if len(passed_subjects) == m:
        # Return the number of days spent
        return days_spent
    else:
        # Not all subjects have been passed, return -1
        return -1

