
def get_min_rest_days(n, activities):
    # Initialize variables
    rest_days = 0
    prev_day_was_contest = False
    prev_day_was_sport = False

    # Iterate through the list of activities
    for day in activities:
        # Check if the day is a contest day
        if day == 1 or day == 3:
            # Check if the previous day was a contest day
            if prev_day_was_contest:
                # Increment the number of rest days
                rest_days += 1
            # Set the flag for the previous day being a contest day
            prev_day_was_contest = True
        # Check if the day is a sport day
        elif day == 2 or day == 0:
            # Check if the previous day was a sport day
            if prev_day_was_sport:
                # Increment the number of rest days
                rest_days += 1
            # Set the flag for the previous day being a sport day
            prev_day_was_sport = True
        # Check if the day is neither a contest nor a sport day
        else:
            # Set both flags to False
            prev_day_was_contest = False
            prev_day_was_sport = False

    # Return the minimum number of rest days
    return rest_days

def main():
    # Read the number of days and the list of activities
    n = int(input())
    activities = list(map(int, input().split()))

    # Call the get_min_rest_days function and print the result
    print(get_min_rest_days(n, activities))

if __name__ == '__main__':
    main()

