
def get_min_rest_days(days, activities):
    # Initialize variables
    rest_days = 0
    last_activity = None

    # Iterate over the days
    for day, activity in zip(days, activities):
        # Check if the current activity is the same as the last activity
        if activity == last_activity:
            # Increment the number of rest days
            rest_days += 1
        # Check if the current activity is different from the last activity
        elif activity != last_activity:
            # Update the last activity
            last_activity = activity

    # Return the minimum number of rest days
    return rest_days

def main():
    # Read the number of days
    days = int(input())

    # Read the activities
    activities = list(map(int, input().split()))

    # Get the minimum number of rest days
    rest_days = get_min_rest_days(days, activities)

    # Print the result
    print(rest_days)

if __name__ == '__main__':
    main()

