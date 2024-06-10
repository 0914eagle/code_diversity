
def get_rest_days(days, gym_open, contests):
    # Initialize variables
    rest_days = 0
    prev_day_sport = False
    prev_day_contest = False

    # Iterate through the days
    for i in range(len(days)):
        # Check if the gym is open on this day
        if gym_open[i] == 1:
            # Check if the contest is carried out on this day
            if contests[i] == 1:
                # If the contest is carried out and the previous day Vasya did not do sport, he can do sport on this day
                if not prev_day_sport:
                    prev_day_sport = True
                # If the contest is carried out and the previous day Vasya did not write the contest, he can write the contest on this day
                elif not prev_day_contest:
                    prev_day_contest = True
                # If the contest is carried out and the previous day Vasya did both sport and write the contest, he will have a rest on this day
                else:
                    rest_days += 1
                    prev_day_sport = False
                    prev_day_contest = False
            # If the contest is not carried out, Vasya can do sport on this day
            else:
                prev_day_sport = True
        # If the gym is closed on this day, Vasya can write the contest on this day
        elif gym_open[i] == 0 and contests[i] == 1:
            prev_day_contest = True
        # If the gym is closed on this day and the contest is not carried out, Vasya will have a rest on this day
        else:
            rest_days += 1
            prev_day_sport = False
            prev_day_contest = False

    return rest_days

def main():
    days = int(input())
    gym_open = list(map(int, input().split()))
    contests = list(map(int, input().split()))
    print(get_rest_days(days, gym_open, contests))

if __name__ == '__main__':
    main()

