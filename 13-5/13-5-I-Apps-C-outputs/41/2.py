
def get_min_rest_days(days_info):
    # Initialize variables to keep track of the number of days Vasya has rest
    rest_days = 0
    # Initialize a variable to keep track of the previous day's activity
    previous_day_activity = None

    for day_info in days_info:
        # Check if the gym is open on this day
        if day_info == 2 or day_info == 3:
            # If the gym is open, Vasya can do sport on this day
            if previous_day_activity == 2 or previous_day_activity == 3:
                # If Vasya did sport on the previous day, he needs a rest today
                rest_days += 1
            previous_day_activity = 2
        else:
            # If the gym is closed, Vasya can write the contest on this day
            if previous_day_activity == 1 or previous_day_activity == 3:
                # If Vasya wrote the contest on the previous day, he needs a rest today
                rest_days += 1
            previous_day_activity = 1

    return rest_days

def main():
    n = int(input())
    days_info = list(map(int, input().split()))
    print(get_min_rest_days(days_info))

if __name__ == '__main__':
    main()

