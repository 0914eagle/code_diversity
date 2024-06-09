
def solve(n, m, a):
    # Initialize variables
    days = 0
    pages_written = 0
    cups_drunk = [0] * n

    # Loop through each day
    while pages_written < m:
        days += 1

        # Loop through each cup of coffee
        for i in range(n):
            # If the cup has not been drunk yet and there is enough caffeine to write a page
            if cups_drunk[i] == 0 and a[i] > 0:
                # Drink the cup and write a page
                cups_drunk[i] = 1
                pages_written += 1
                a[i] -= 1

                # If all the pages have been written, return the number of days
                if pages_written == m:
                    return days

    # If all the days have been used and not all the pages have been written, return -1
    return -1

