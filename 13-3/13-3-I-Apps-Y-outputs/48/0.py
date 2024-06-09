
def get_min_days(n, m, a):
    # Initialize variables
    days = 0
    pages_written = 0
    cups_drunk = [0] * n

    # Loop through each day
    while pages_written < m:
        days += 1

        # Loop through each cup
        for i in range(n):
            # If the cup has not been drunk and there is still work to be done, drink the cup
            if cups_drunk[i] == 0 and pages_written < m:
                cups_drunk[i] = 1
                pages_written += a[i]

        # If all cups have been drunk and there is still work to be done, return -1
        if all(cups_drunk) and pages_written < m:
            return -1

    return days

