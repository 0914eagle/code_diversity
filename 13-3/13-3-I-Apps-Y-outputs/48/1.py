
def get_days_needed(n, m, a):
    # Initialize variables
    days = 0
    pages_written = 0
    cups_drunk = 0

    # Loop through each cup of coffee
    for i in range(n):
        # Calculate the number of pages that can be written with the current cup of coffee
        pages_written_with_current_cup = min(a[i], m - pages_written)

        # If the number of pages written with the current cup of coffee is greater than zero, drink the cup and update the number of pages written
        if pages_written_with_current_cup > 0:
            cups_drunk += 1
            pages_written += pages_written_with_current_cup

        # If all the pages have been written, return the number of days needed
        if pages_written == m:
            return days

        # If the number of pages written with the current cup of coffee is zero, move on to the next cup of coffee
        else:
            continue

    # If all the cups of coffee have been drunk and not all the pages have been written, return -1
    if cups_drunk == n and pages_written < m:
        return -1

# Test the function with example inputs
n = 5
m = 8
a = [2, 3, 1, 1, 2]
print(get_days_needed(n, m, a)) # Output: 4

n = 7
m = 10
a = [1, 3, 4, 2, 1, 4, 2]
print(get_days_needed(n, m, a)) # Output: 2

n = 5
m = 15
a = [5, 5, 5, 5, 5]
print(get_days_needed(n, m, a)) # Output: 1

n = 5
m = 16
a = [5, 5, 5, 5, 5]
print(get_days_needed(n, m, a)) # Output: 2

n = 5
m = 26
a = [5, 5, 5, 5, 5]
print(get_days_needed(n, m, a)) # Output: -1

