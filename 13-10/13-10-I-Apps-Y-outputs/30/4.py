
def get_hours_until_new_year(hour):
    if hour < 24:
        return 24 - hour
    else:
        return 24 + (24 - hour)

def main():
    hour = int(input())
    hours_until_new_year = get_hours_until_new_year(hour)
    print(f"We have {hours_until_new_year} hours until New Year at {hour}:00 on 30th, December.")

if __name__ == '__main__':
    main()

