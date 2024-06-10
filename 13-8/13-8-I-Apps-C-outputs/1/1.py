
def get_surprise_penalty(year, month, day):
    # Calculate the surprise penalty for the given date
    if year == 2018:
        return 0
    else:
        return (month * 100 + day - (10 * 12)) ** 2

def get_schedule(forbidden_dates, years):
    # Initialize the schedule with the date of the previous year
    schedule = [(2018, 10, 12)]

    # Iterate through the years
    for year in range(2019, 2018 + years + 1):
        # Get the date of Canadian Thanksgiving for the current year
        thanksgiving = get_canadian_thanksgiving(year)

        # Check if the date is forbidden
        if (year, 10, thanksgiving) in forbidden_dates:
            # If it is forbidden, find the next available date after the current year
            date = get_next_available_date(schedule, year, 10, thanksgiving)
        else:
            # If it is not forbidden, use the date of Canadian Thanksgiving
            date = (year, 10, thanksgiving)

        # Add the date to the schedule
        schedule.append(date)

    # Return the schedule
    return schedule

def get_canadian_thanksgiving(year):
    # Get the date of Canadian Thanksgiving for the given year
    if year == 2018:
        return 11
    else:
        return (year - 2018) % 7 + 11

def get_next_available_date(schedule, year, month, day):
    # Find the next available date after the current year
    date = (year, month, day)
    while date in schedule:
        date = (date[0] + 1, date[1], date[2])
    return date

def main():
    # Read the input
    years, forbidden_dates = read_input()

    # Get the schedule
    schedule = get_schedule(forbidden_dates, years)

    # Calculate the total surprise penalty
    total_penalty = 0
    for i in range(len(schedule) - 1):
        total_penalty += get_surprise_penalty(schedule[i + 1][0], schedule[i + 1][1], schedule[i + 1][2])

    # Print the output
    print(total_penalty)
    for date in schedule:
        print(date[0], date[1], date[2])

def read_input():
    # Read the number of years and forbidden dates
    years = int(input())
    forbidden_dates = int(input())

    # Read the forbidden dates
    dates = []
    for i in range(forbidden_dates):
        dates.append(tuple(map(int, input().split())))

    # Return the number of years and the list of forbidden dates
    return years, dates

if __name__ == '__main__':
    main()

