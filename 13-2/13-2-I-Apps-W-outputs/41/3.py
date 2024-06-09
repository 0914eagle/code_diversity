
def solve(n, m, d, a):
    # Initialize a dictionary to store the number of days needed to pass each subject
    days_needed = {}
    for i in range(m):
        days_needed[i+1] = a[i]

    # Initialize a set to store the passed subjects
    passed_subjects = set()

    # Initialize the number of days spent preparing
    days_spent = 0

    # Loop through each day
    for i in range(n):
        # If the current day is allowed to pass an exam
        if d[i] != 0:
            # If the current day is not already spent preparing for a subject
            if d[i] not in passed_subjects:
                # Spend the day preparing for the current subject
                days_spent += 1
                passed_subjects.add(d[i])
            # If the current day is already spent preparing for a subject
            else:
                # Pass the exam on the current day
                days_spent += 1
                passed_subjects.remove(d[i])

    # If all subjects have been passed, return the number of days spent
    if len(passed_subjects) == 0:
        return days_spent
    # If not all subjects have been passed, return -1
    else:
        return -1

