
def get_min_rest_days(days, gym_info, contests):
    # Initialize variables
    rest_days = 0
    consecutive_sport_days = 0
    consecutive_contest_days = 0
    
    # Iterate through the days
    for i in range(len(days)):
        # Check if the gym is open on this day
        if gym_info[i] == 1 or gym_info[i] == 3:
            # Check if the contest is carried out on this day
            if contests[i] == 1 or contests[i] == 3:
                # Vasya can do sport and write the contest on this day
                consecutive_sport_days = 0
                consecutive_contest_days = 0
            else:
                # Vasya can do sport on this day
                consecutive_sport_days += 1
                consecutive_contest_days = 0
        else:
            # Check if the contest is carried out on this day
            if contests[i] == 1 or contests[i] == 2:
                # Vasya can write the contest on this day
                consecutive_sport_days = 0
                consecutive_contest_days += 1
            else:
                # Vasya can do rest on this day
                consecutive_sport_days = 0
                consecutive_contest_days = 0
        
        # Check if Vasya has to rest
        if consecutive_sport_days >= 2 or consecutive_contest_days >= 2:
            rest_days += 1
    
    return rest_days

def main():
    days = int(input())
    gym_info = list(map(int, input().split()))
    contests = list(map(int, input().split()))
    print(get_min_rest_days(days, gym_info, contests))

if __name__ == '__main__':
    main()

