
def get_days_needed(n, m, a):
    # Initialize variables
    days = 0
    pages_written = 0
    cups_drunk = 0

    # Sort the cups of coffee by caffeine dosage in descending order
    sorted_cups = sorted(a, reverse=True)

    # Loop through each cup of coffee and determine how many pages can be written
    for cup in sorted_cups:
        # Check if the current cup of coffee can be drunk
        if cup <= pages_written:
            # Drink the current cup of coffee and update the number of pages written
            pages_written += cup
            cups_drunk += 1
        else:
            # The current cup of coffee cannot be drunk, break the loop
            break

    # Calculate the number of days needed to write the coursework
    days = cups_drunk

    # Check if the coursework can be completed in the given number of days
    if pages_written < m:
        # The coursework cannot be completed in the given number of days
        days = -1

    return days

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_days_needed(n, m, a))

