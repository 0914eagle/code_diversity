
def get_hours_until_new_year(m):
    current_time = datetime.datetime.now()
    current_day = current_time.day
    current_month = current_time.month
    current_year = current_time.year
    new_year_day = 1
    new_year_month = 1
    new_year_year = current_year + 1
    if current_month == 12 and current_day >= 30:
        new_year_month = 1
        new_year_day = 1
    else:
        new_year_month = current_month
        new_year_day = current_day + 1
    new_year_time = datetime.datetime(new_year_year, new_year_month, new_year_day, m, 0, 0)
    hours_until_new_year = (new_year_time - current_time).total_seconds() / 3600
    return int(hours_until_new_year)

def main():
    m = int(input())
    hours_until_new_year = get_hours_until_new_year(m)
    print(f"We have {hours_until_new_year} hours until New Year at {m}:00 on 30th, December.")

if __name__ == '__main__':
    main()

