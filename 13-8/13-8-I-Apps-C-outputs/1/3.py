
def get_surprise_penalty(schedule):
    # Calculate the surprise penalty for the given schedule
    penalty = 0
    for i in range(len(schedule) - 1):
        x = schedule[i]
        y = schedule[i + 1]
        penalty += (x - y) ** 2
    return penalty

def get_possible_dates(forbidden_dates):
    # Get all possible dates in October between 2019 and 2118 that are not forbidden
    possible_dates = []
    for year in range(2019, 2119):
        for day in range(1, 32):
            date = f"{year} 10 {day}"
            if date not in forbidden_dates:
                possible_dates.append(date)
    return possible_dates

def get_schedule(forbidden_dates, num_years):
    # Get the best schedule for the given number of years and forbidden dates
    possible_dates = get_possible_dates(forbidden_dates)
    schedules = []
    for i in range(len(possible_dates) - num_years + 1):
        schedule = possible_dates[i:i+num_years]
        schedules.append(schedule)
    return min(schedules, key=get_surprise_penalty)

def main():
    num_years = int(input())
    num_forbidden_dates = int(input())
    forbidden_dates = []
    for _ in range(num_forbidden_dates):
        year, month, day = map(int, input().split())
        date = f"{year} {month} {day}"
        forbidden_dates.append(date)
    schedule = get_schedule(forbidden_dates, num_years)
    print(get_surprise_penalty(schedule))
    for date in schedule:
        print(date)

if __name__ == '__main__':
    main()

