
def get_min_rest_days(days):
    # Initialize variables
    rest_days = 0
    last_day_sport = -1
    last_day_contest = -1
    
    # Iterate through the days
    for day in days:
        # Check if the gym is open and a contest is carried out
        if day == 3 or day == 2:
            # If the gym is open and a contest is carried out, increment the rest days
            rest_days += 1
            # Update the last day of sport and contest
            last_day_sport = day
            last_day_contest = day
        # Check if the gym is closed and a contest is carried out
        elif day == 1:
            # If the gym is closed and a contest is carried out, increment the rest days
            rest_days += 1
            # Update the last day of contest
            last_day_contest = day
        # Check if the gym is open and no contest is carried out
        elif day == 0:
            # If the gym is open and no contest is carried out, do sport on this day
            if last_day_sport != day - 1:
                rest_days += 1
                last_day_sport = day
    
    return rest_days

def main():
    # Read the number of days
    days = int(input())
    # Read the sequence of days
    days_sequence = list(map(int, input().split()))
    # Get the minimum number of rest days
    rest_days = get_min_rest_days(days_sequence)
    # Print the minimum number of rest days
    print(rest_days)

if __name__ == '__main__':
    main()

