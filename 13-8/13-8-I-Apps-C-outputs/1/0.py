
def get_surprise_penalty(year, month, day):
    if year == 2018:
        return 0
    previous_year = year - 1
    previous_month = month
    previous_day = day
    if month == 10:
        previous_month = 10
        previous_day = day
    elif month == 11:
        previous_month = 11
        previous_day = day
    elif month == 12:
        previous_month = 12
        previous_day = day
    elif month == 1:
        previous_month = 1
        previous_day = day
    elif month == 2:
        previous_month = 2
        previous_day = day
    elif month == 3:
        previous_month = 3
        previous_day = day
    elif month == 4:
        previous_month = 4
        previous_day = day
    elif month == 5:
        previous_month = 5
        previous_day = day
    elif month == 6:
        previous_month = 6
        previous_day = day
    elif month == 7:
        previous_month = 7
        previous_day = day
    elif month == 8:
        previous_month = 8
        previous_day = day
    elif month == 9:
        previous_month = 9
        previous_day = day
    elif month == 10:
        previous_month = 10
        previous_day = day
    surprise_penalty = (previous_month - month) ** 2 + (previous_day - day) ** 2
    return surprise_penalty

def get_best_schedule(forbidden_dates):
    # Initialize a list to store the best schedule
    best_schedule = []
    # Initialize a variable to store the smallest total surprise penalty
    smallest_penalty = float('inf')
    # Iterate through all possible dates
    for year in range(2019, 2401):
        for month in range(1, 13):
            for day in range(1, 32):
                # Check if the date is not a forbidden date
                if (year, month, day) not in forbidden_dates:
                    # Calculate the surprise penalty for the date
                    surprise_penalty = get_surprise_penalty(year, month, day)
                    # Check if the surprise penalty is smaller than the smallest penalty
                    if surprise_penalty < smallest_penalty:
                        # If it is, update the best schedule and smallest penalty
                        best_schedule = [(year, month, day)]
                        smallest_penalty = surprise_penalty
                    # Check if the surprise penalty is the same as the smallest penalty
                    elif surprise_penalty == smallest_penalty:
                        # If it is, add the date to the best schedule
                        best_schedule.append((year, month, day))
    return best_schedule

def main():
    # Read the number of years and forbidden dates from stdin
    num_years = int(input())
    num_forbidden_dates = int(input())
    forbidden_dates = []
    for _ in range(num_forbidden_dates):
        year, month, day = map(int, input().split())
        forbidden_dates.append((year, month, day))
    # Get the best schedule
    best_schedule = get_best_schedule(forbidden_dates)
    # Print the smallest total surprise penalty
    print(smallest_penalty)
    # Print the best schedule
    for year, month, day in best_schedule:
        print(f"{year} {month} {day}")

if __name__ == '__main__':
    main()

