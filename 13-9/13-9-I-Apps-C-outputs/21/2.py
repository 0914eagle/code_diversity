
def get_min_rest_days(n, activities):
    # Initialize variables
    rest_days = 0
    prev_activity = None

    # Iterate through the list of activities
    for activity in activities:
        # If the current activity is different from the previous activity
        if activity != prev_activity:
            # Increment the number of rest days
            rest_days += 1
        # Update the previous activity
        prev_activity = activity

    # Return the minimum number of rest days
    return rest_days

def main():
    # Read the number of days and the list of activities from stdin
    n = int(input())
    activities = list(map(int, input().split()))

    # Call the get_min_rest_days function and print the result
    print(get_min_rest_days(n, activities))

if __name__ == '__main__':
    main()

