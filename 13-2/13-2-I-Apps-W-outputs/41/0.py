
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
            # If the current day is not the last day
            if i != n-1:
                # If the current day is not the first day
                if i != 0:
                    # If the previous day is allowed to pass an exam
                    if d[i-1] != 0:
                        # If the previous day is not passed, pass it
                        if d[i-1] not in passed_subjects:
                            passed_subjects.add(d[i-1])
                            days_spent += 1

                # If the current day is not passed, pass it
                if d[i] not in passed_subjects:
                    passed_subjects.add(d[i])
                    days_spent += 1

            # If the current day is the last day
            else:
                # If the current day is allowed to pass an exam
                if d[i] != 0:
                    # If the current day is not passed, pass it
                    if d[i] not in passed_subjects:
                        passed_subjects.add(d[i])
                        days_spent += 1

        # If the current day is not allowed to pass an exam
        else:
            # If the previous day is allowed to pass an exam
            if i != 0 and d[i-1] != 0:
                # If the previous day is not passed, pass it
                if d[i-1] not in passed_subjects:
                    passed_subjects.add(d[i-1])
                    days_spent += 1

    # If all subjects are passed, return the number of days spent
    if len(passed_subjects) == m:
        return days_spent

    # If not all subjects are passed, return -1
    return -1

