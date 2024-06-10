
def get_forbidden_dates(number_of_dates):
    forbidden_dates = []
    for _ in range(number_of_dates):
        year, month, day = map(int, input().split())
        forbidden_dates.append((year, month, day))
    return forbidden_dates

def get_surprise_penalty(chosen_dates, forbidden_dates):
    surprise_penalty = 0
    for i in range(len(chosen_dates)):
        year, month, day = chosen_dates[i]
        if (year, month, day) in forbidden_dates:
            continue
        previous_year, previous_month, previous_day = chosen_dates[(i - 1) % len(chosen_dates)]
        surprise_penalty += (day - previous_day) ** 2
    return surprise_penalty

def choose_dates(number_of_years, forbidden_dates):
    chosen_dates = [(2018, 10, 12)]
    for i in range(number_of_years - 1):
        year, month, day = chosen_dates[i]
        next_year = year + 1
        next_month = month
        next_day = day
        while (next_year, next_month, next_day) in forbidden_dates:
            next_day += 1
            if next_day > 31:
                next_month += 1
                next_day = 1
                if next_month > 10:
                    next_month = 10
                    next_year += 1
        chosen_dates.append((next_year, next_month, next_day))
    return chosen_dates

def main():
    number_of_years = int(input())
    forbidden_dates = get_forbidden_dates(int(input()))
    chosen_dates = choose_dates(number_of_years, forbidden_dates)
    surprise_penalty = get_surprise_penalty(chosen_dates, forbidden_dates)
    print(surprise_penalty)
    for year, month, day in chosen_dates:
        print(f"{year} {month} {day:02}")

if __name__ == "__main__":
    main()

