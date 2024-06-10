
def get_hours_until_new_year(hour):
    current_time = datetime.datetime.now()
    new_year_time = datetime.datetime(current_time.year, 12, 30, hour, 0, 0)
    if new_year_time < current_time:
        new_year_time += datetime.timedelta(days=1)
    return (new_year_time - current_time).total_seconds() // 3600

def main():
    hour = int(input())
    hours_until_new_year = get_hours_until_new_year(hour)
    print(f"We have {hours_until_new_year} hours until New Year at {hour}:00 on 30th, December.")

if __name__ == '__main__':
    main()

