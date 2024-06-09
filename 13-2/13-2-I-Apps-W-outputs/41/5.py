
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
                        # If the previous day is not the last day
                        if i-1 != n-1:
                            # If the previous day is not the first day
                            if i-1 != 0:
                                # If the previous day is allowed to pass the same exam
                                if d[i-1] == d[i]:
                                    # Pass the exam on the current day
                                    passed_subjects.add(d[i])
                                    # Remove the exam from the days needed to pass
                                    days_needed.pop(d[i])
                                    # Spend a day preparing for the exam
                                    days_spent += 1
                                    # Continue to the next day
                                    continue
            # If the current day is the last day
            if i == n-1:
                # If the current day is allowed to pass an exam
                if d[i] != 0:
                    # Pass the exam on the current day
                    passed_subjects.add(d[i])
                    # Remove the exam from the days needed to pass
                    days_needed.pop(d[i])
                    # Spend a day preparing for the exam
                    days_spent += 1
                    # Continue to the next day
                    continue
        # If the current day is not allowed to pass an exam
        else:
            # Spend a day preparing for the exam
            days_spent += 1
            # Continue to the next day
            continue

    # If all subjects have been passed
    if len(days_needed) == 0:
        # Return the number of days spent preparing
        return days_spent
    # If not all subjects have been passed
    else:
        # Return -1
        return -1

n, m = map(int, input().split())
d = list(map(int, input().split()))
a = list(map(int, input().split()))
print(solve(n, m, d, a))

