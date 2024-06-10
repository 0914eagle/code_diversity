
import itertools

def get_forbidden_dates(F):
    forbidden_dates = []
    for i in range(F):
        year, month, day = map(int, input().split())
        forbidden_dates.append((year, month, day))
    return forbidden_dates

def get_allowed_dates(forbidden_dates):
    allowed_dates = []
    for year in range(2019, 2119):
        for day in range(1, 32):
            date = (year, 10, day)
            if date not in forbidden_dates:
                allowed_dates.append(date)
    return allowed_dates

def get_surprise_penalty(date1, date2):
    penalty = 0
    if date1[2] != date2[2]:
        penalty += abs(date1[2] - date2[2]) ** 2
    if date1[0] != date2[0]:
        penalty += abs(date1[0] - date2[0])
    return penalty

def schedule_contest(Z, forbidden_dates):
    allowed_dates = get_allowed_dates(forbidden_dates)
    previous_date = (2018, 10, 12)
    total_penalty = 0
    schedule = []
    for i in range(Z):
        min_penalty = float('inf')
        min_date = None
        for date in allowed_dates:
            penalty = get_surprise_penalty(previous_date, date)
            if penalty < min_penalty:
                min_penalty = penalty
                min_date = date
        total_penalty += min_penalty
        schedule.append(min_date)
        previous_date = min_date
    return total_penalty, schedule

def main():
    Z = int(input())
    F = int(input())
    forbidden_dates = get_forbidden_dates(F)
    total_penalty, schedule = schedule_contest(Z, forbidden_dates)
    print(total_penalty)
    for date in schedule:
        print(date[0], 10, date[2])

if __name__ == '__main__':
    main()

