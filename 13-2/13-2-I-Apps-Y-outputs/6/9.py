
def get_days(n, m, a):
    # Initialize variables
    days = 0
    pages_written = 0
    cups_drunk = 0

    # Sort the cups of coffee by caffeine dosage in descending order
    a.sort(reverse=True)

    # Loop through each cup of coffee
    for i in range(n):
        # If the current cup of coffee has enough caffeine to write at least one page,
        # drink it and write as many pages as possible
        if a[i] > 0:
            cups_drunk += 1
            pages_written += min(a[i], m - pages_written)
            m -= pages_written

        # If all pages have been written, break the loop
        if m == 0:
            break

    # If all pages have been written, return the number of days
    # otherwise, return -1
    if m == 0:
        return days
    else:
        return -1

