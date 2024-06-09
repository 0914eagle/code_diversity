
def get_number_of_days(n, m, a):
    # Initialize variables
    days = 0
    pages_written = 0
    cups_drunk = 0

    # Sort the cups of coffee by caffeine dosage in descending order
    sorted_cups = sorted(a, reverse=True)

    # Loop through each cup of coffee and determine the number of pages that can be written
    for cup in sorted_cups:
        pages_written += cup
        cups_drunk += 1
        if pages_written >= m:
            break

    # Calculate the number of days needed to write the coursework
    days = cups_drunk

    # Check if it is possible to write the coursework in the given number of days
    if pages_written < m:
        days = -1

    return days

