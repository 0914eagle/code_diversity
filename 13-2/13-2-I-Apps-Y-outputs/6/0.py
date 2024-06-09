
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
        # drink it and write the maximum number of pages possible
        if a[i] > 0:
            cups_drunk += 1
            pages_written += min(m - pages_written, a[i])

        # If all pages have been written, return the number of days
        if pages_written == m:
            return days

        # If not all pages have been written, increment the number of days
        days += 1

    # If all cups of coffee have been drunk and not all pages have been written,
    # it is impossible to write the coursework, so return -1
    if cups_drunk == n and pages_written < m:
        return -1

# Test the function with example inputs
n = 5
m = 8
a = [2, 3, 1, 1, 2]
print(get_days(n, m, a)) # should print 4

n = 7
m = 10
a = [1, 3, 4, 2, 1, 4, 2]
print(get_days(n, m, a)) # should print 2

n = 5
m = 15
a = [5, 5, 5, 5, 5]
print(get_days(n, m, a)) # should print 1

n = 5
m = 16
a = [5, 5, 5, 5, 5]
print(get_days(n, m, a)) # should print 2

n = 5
m = 26
a = [5, 5, 5, 5, 5]
print(get_days(n, m, a)) # should print -1

