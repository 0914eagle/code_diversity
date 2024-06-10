
def get_min_rest_days(n, a):
    # Initialize variables
    rest_days = 0
    last_day_type = None

    # Iterate over the days
    for i in range(n):
        # Get the type of the current day
        current_day_type = a[i]

        # Check if the current day is the same as the last day
        if current_day_type == last_day_type:
            # If it is the same, increase the rest days count
            rest_days += 1

        # Check if the current day is different from the last day
        elif current_day_type != last_day_type:
            # If it is different, set the last day type to the current day type
            last_day_type = current_day_type

    # Return the minimum rest days count
    return rest_days

def main():
    # Get the number of days and the day types
    n = int(input())
    a = list(map(int, input().split()))

    # Call the get_min_rest_days function and print the result
    print(get_min_rest_days(n, a))

if __name__ == '__main__':
    main()

