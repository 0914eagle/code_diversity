
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
                # Check if the current day is the last day to pass the current subject
                if days_needed[d[i]] == 1:
                    # Add the current subject to the passed subjects set
                    passed_subjects.add(d[i])
                    # Remove the current subject from the days needed dictionary
                    del days_needed[d[i]]
                # Otherwise, decrease the number of days needed to pass the current subject by 1
                else:
                    days_needed[d[i]] -= 1
            # If the current day is the last day
            else:
                # Check if the current day is the last day to pass the current subject
                if days_needed[d[i]] == 1:
                    # Add the current subject to the passed subjects set
                    passed_subjects.add(d[i])
                    # Remove the current subject from the days needed dictionary
                    del days_needed[d[i]]
                # Otherwise, return -1 because it is impossible to pass all exams
                else:
                    return -1
        # If the current day is not allowed to pass an exam
        else:
            # Increase the number of days spent preparing by 1
            days_spent += 1

    # Check if all subjects have been passed
    if len(passed_subjects) == m:
        # Return the number of days spent preparing
        return days_spent
    # Otherwise, return -1 because it is impossible to pass all exams
    else:
        return -1

