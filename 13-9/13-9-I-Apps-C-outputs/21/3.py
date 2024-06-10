
def get_minimum_rest_days(days, gym_and_contest):
    # Initialize variables
    rest_days = 0
    previous_day_gym_open = False
    previous_day_contest_held = False

    # Iterate through the days
    for day in days:
        gym_open, contest_held = gym_and_contest[day]

        # Check if the gym is open and a contest is held on the current day
        if gym_open and contest_held:
            # If the gym is open and a contest is held on the current day, Vasya can do sport or write the contest
            if previous_day_gym_open and previous_day_contest_held:
                # If Vasya did sport or write the contest on the previous day, he needs a rest
                rest_days += 1
            previous_day_gym_open = True
            previous_day_contest_held = True

        # Check if the gym is open but no contest is held on the current day
        elif gym_open and not contest_held:
            # If the gym is open but no contest is held on the current day, Vasya can do sport
            if previous_day_gym_open and previous_day_contest_held:
                # If Vasya did sport or write the contest on the previous day, he needs a rest
                rest_days += 1
            previous_day_gym_open = True
            previous_day_contest_held = False

        # Check if the gym is closed and a contest is held on the current day
        elif not gym_open and contest_held:
            # If the gym is closed and a contest is held on the current day, Vasya can write the contest
            if previous_day_gym_open and previous_day_contest_held:
                # If Vasya did sport or write the contest on the previous day, he needs a rest
                rest_days += 1
            previous_day_gym_open = False
            previous_day_contest_held = True

        # Check if the gym is closed and no contest is held on the current day
        else:
            # If the gym is closed and no contest is held on the current day, Vasya can do rest
            if previous_day_gym_open and previous_day_contest_held:
                # If Vasya did sport or write the contest on the previous day, he needs a rest
                rest_days += 1
            previous_day_gym_open = False
            previous_day_contest_held = False

    return rest_days

def main():
    days = [1, 3, 2, 0]
    gym_and_contest = [(True, False), (False, True), (True, False), (False, False)]
    print(get_minimum_rest_days(days, gym_and_contest))

if __name__ == '__main__':
    main()

