
def get_min_days_rest(n, days):
    # Initialize variables
    rest_days = 0
    last_day_sport = 0
    last_day_contest = 0

    # Iterate through the days
    for day in days:
        # Check if the gym is open and a contest is carried out
        if day == 3 or day == 2:
            # If the gym is open and a contest is carried out, increment the rest days
            rest_days += 1
            # Set the last day of sport and contest to the current day
            last_day_sport = day
            last_day_contest = day
        # Check if the gym is open and no contest is carried out
        elif day == 1:
            # If the gym is open and no contest is carried out, set the last day of sport to the current day
            last_day_sport = day
        # Check if the gym is closed and a contest is carried out
        elif day == 0:
            # If the gym is closed and a contest is carried out, set the last day of contest to the current day
            last_day_contest = day

    # Return the minimum number of rest days
    return rest_days

def main():
    # Read the number of days and the sequence of days
    n = int(input())
    days = list(map(int, input().split()))

    # Call the function to get the minimum number of rest days
    rest_days = get_min_days_rest(n, days)

    # Print the minimum number of rest days
    print(rest_days)

if __name__ == '__main__':
    main()

