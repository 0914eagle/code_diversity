
def get_hours_until_new_year(hour):
    current_hour = int(hour)
    if current_hour < 24:
        return 24 - current_hour
    else:
        return 0

def main():
    hour = input("Enter the hour: ")
    hours_until_new_year = get_hours_until_new_year(hour)
    print(f"We have {hours_until_new_year} hours until New Year at {hour} o'clock on 30th, December.")

if __name__ == '__main__':
    main()

