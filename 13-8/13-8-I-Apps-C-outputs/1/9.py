
def get_schedule(Z, F, forbidden_dates):
    # Initialize the schedule as a list of None values
    schedule = [None] * Z

    # Set the initial date for the schedule
    date = datetime.date(2018, 10, 12)

    # Loop through each year
    for i in range(Z):
        # Check if the date is a forbidden date
        if date not in forbidden_dates:
            # If not, add it to the schedule
            schedule[i] = date

        # Increment the date by one day
        date += datetime.timedelta(days=1)

    # Return the schedule
    return schedule

def get_surprise_penalty(schedule):
    # Initialize the surprise penalty to 0
    penalty = 0

    # Loop through each year in the schedule
    for i in range(len(schedule) - 1):
        # Calculate the surprise penalty for the current year
        penalty += (schedule[i].day - schedule[i + 1].day) ** 2

    # Return the surprise penalty
    return penalty

def main():
    # Read the input data
    Z, F = map(int, input().split())
    forbidden_dates = []
    for i in range(F):
        year, month, day = map(int, input().split())
        forbidden_dates.append(datetime.date(year, month, day))

    # Get the optimal schedule
    schedule = get_schedule(Z, F, forbidden_dates)

    # Calculate the surprise penalty for the optimal schedule
    penalty = get_surprise_penalty(schedule)

    # Print the output
    print(penalty)
    for date in schedule:
        print(date.strftime("%Y %m %d"))

if __name__ == '__main__':
    main()

