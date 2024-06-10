
def get_rest_days(n, days):
    # Initialize variables
    rest_days = 0
    prev_day = 0

    # Iterate through the days
    for day in days:
        # If the day is the same as the previous day, increase the rest days
        if day == prev_day:
            rest_days += 1
        # If the day is different from the previous day, reset the rest days
        else:
            rest_days = 0
        # Update the previous day
        prev_day = day

    # Return the minimum number of rest days
    return rest_days

def main():
    # Read the number of days and the list of days
    n = int(input())
    days = list(map(int, input().split()))

    # Get the minimum number of rest days
    rest_days = get_rest_days(n, days)

    # Print the minimum number of rest days
    print(rest_days)

if __name__ == '__main__':
    main()

