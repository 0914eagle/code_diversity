
def get_days_needed(n, m, a):
    # Initialize variables
    days = 0
    pages_written = 0
    cups_drunk = 0

    # Sort the cups of coffee by caffeine dosage in descending order
    sorted_cups = sorted(a, reverse=True)

    # Loop through each cup of coffee and determine how many pages can be written
    for cup in sorted_cups:
        # Calculate the number of pages that can be written with the current cup of coffee
        pages_written_with_cup = min(m - pages_written, cup)

        # Update the number of pages written and the number of cups drunk
        pages_written += pages_written_with_cup
        cups_drunk += 1

        # If all pages have been written, break the loop
        if pages_written == m:
            break

    # Return the number of days needed to write the coursework
    return days

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_days_needed(n, m, a))

