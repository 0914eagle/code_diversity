
import sys

def get_input():
    Z = int(input())
    F = int(input())
    forbidden_dates = []
    for i in range(F):
        year, month, day = map(int, input().split())
        forbidden_dates.append((year, month, day))
    return Z, F, forbidden_dates

def get_surprise_penalty(date, previous_date):
    x, y = date[2], previous_date[2]
    return (x-y)**2

def get_schedule(Z, F, forbidden_dates):
    # Initialize the schedule with the previous date
    schedule = [(2018, 10, 12)]
    for i in range(Z):
        # Get the current date
        current_date = schedule[i]
        # Get the previous date
        previous_date = schedule[i-1] if i > 0 else (2018, 10, 12)
        # Get the surprise penalty for the current date
        surprise_penalty = get_surprise_penalty(current_date, previous_date)
        # Loop through the forbidden dates and find the first date that is not a forbidden date
        for j in range(F):
            date = (current_date[0] + 1, 10, current_date[2])
            if date not in forbidden_dates:
                break
        # Add the date to the schedule
        schedule.append(date)
    return schedule

def main():
    Z, F, forbidden_dates = get_input()
    schedule = get_schedule(Z, F, forbidden_dates)
    print(get_surprise_penalty(schedule[-1], schedule[-2]))
    for date in schedule:
        print(date[0], date[1], date[2])

if __name__ == '__main__':
    main()

