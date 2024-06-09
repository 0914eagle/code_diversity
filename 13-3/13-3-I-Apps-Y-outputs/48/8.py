
def get_min_days(n, m, a):
    # Initialize variables
    days = 0
    pages_written = 0
    cups_drunk = [0] * n

    # Loop through each day
    while pages_written < m:
        days += 1

        # Loop through each cup of coffee
        for i in range(n):
            # If the cup of coffee has not been drunk yet and there are still pages to write
            if cups_drunk[i] == 0 and pages_written < m:
                # Drink the cup of coffee and write the maximum number of pages possible
                cups_drunk[i] = 1
                pages_written += max(0, a[i] - days + 1)

    # If all pages have been written, return the number of days
    if pages_written == m:
        return days
    else:
        return -1

