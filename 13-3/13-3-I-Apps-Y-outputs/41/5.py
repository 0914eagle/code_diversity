
def get_hours_until_new_year(hour):
    current_hour = int(hour)
    hours_until_new_year = 24 - current_hour
    return hours_until_new_year

if __name__ == '__main__':
    hour = input()
    hours_until_new_year = get_hours_until_new_year(hour)
    print(f"We have {hours_until_new_year} hours until New Year at {hour} o'clock on 30th, December.")

