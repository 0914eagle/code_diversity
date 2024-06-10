
def get_hours_until_new_year(hour):
    current_time = datetime.datetime.now()
    new_year_time = datetime.datetime(current_time.year, 12, 30, hour, 0, 0)
    if new_year_time < current_time:
        new_year_time = new_year_time + datetime.timedelta(days=1)
    return (new_year_time - current_time).seconds // 3600

def main():
    hour = int(input())
    print(get_hours_until_new_year(hour))

if __name__ == '__main__':
    main()

