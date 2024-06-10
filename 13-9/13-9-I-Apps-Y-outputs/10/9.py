
def get_hours_until_new_year(hour):
    current_hour = int(hour)
    if current_hour < 0 or current_hour > 23:
        raise ValueError("Invalid input")
    return 24 - current_hour

def main():
    hour = input("Enter the hour: ")
    try:
        hours_until_new_year = get_hours_until_new_year(hour)
        print(f"We have {hours_until_new_year} hours until New Year at {hour} o'clock on 30th, December.")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()

