
import itertools

def get_forbidden_dates(number_of_forbidden_dates):
    forbidden_dates = []
    for _ in range(number_of_forbidden_dates):
        year, month, day = map(int, input().split())
        forbidden_dates.append((year, month, day))
    return forbidden_dates

def get_possible_dates(year, month, day, forbidden_dates):
    possible_dates = []
    for date in itertools.product(range(1, 32), range(1, 13), range(year, year + 100)):
        if date[1] == month and date[2] == day and date not in forbidden_dates:
            possible_dates.append(date)
    return possible_dates

def get_surprise_penalty(year, month, day, previous_year, previous_month, previous_day):
    if month == previous_month and day == previous_day:
        return 0
    else:
        return (day - previous_day) ** 2

def schedule_contest(number_of_years, forbidden_dates):
    previous_year = 2018
    previous_month = 10
    previous_day = 12
    surprise_penalty = 0
    schedule = []
    for _ in range(number_of_years):
        possible_dates = get_possible_dates(previous_year + 1, previous_month, previous_day, forbidden_dates)
        if not possible_dates:
            return -1
        current_date = min(possible_dates, key=lambda x: get_surprise_penalty(x[0], x[1], x[2], previous_year, previous_month, previous_day))
        surprise_penalty += get_surprise_penalty(current_date[0], current_date[1], current_date[2], previous_year, previous_month, previous_day)
        schedule.append(current_date)
        previous_year, previous_month, previous_day = current_date
    return surprise_penalty, schedule

def main():
    number_of_years = int(input())
    number_of_forbidden_dates = int(input())
    forbidden_dates = get_forbidden_dates(number_of_forbidden_dates)
    surprise_penalty, schedule = schedule_contest(number_of_years, forbidden_dates)
    print(surprise_penalty)
    for date in schedule:
        print('{} {} {}'.format(date[0], date[1], date[2]))

if __name__ == '__main__':
    main()

