
def get_hours_until_new_year(hour):
    current_hour = int(hour)
    hours_until_new_year = 24 - current_hour
    return hours_until_new_year

def main():
    hour = input("Enter the current hour (in 24-hour notation): ")
    hours_until_new_year = get_hours_until_new_year(hour)
    print(f"We have {hours_until_new_year} hours until New Year at {hour} o'clock on December 30th.")

if __name__ == '__main__':
    main()

