
def get_min_rest_days(days, activities):
    # Initialize variables
    rest_days = 0
    last_activity = None

    # Iterate through the days
    for day in days:
        # Check if the gym is open and a contest is carried out
        if activities[day] in [2, 3]:
            # If the gym is open and a contest is carried out, Vasya can do sport
            if last_activity != "sport":
                rest_days += 1
                last_activity = "sport"
        else:
            # If the gym is closed or a contest is not carried out, Vasya can write the contest
            if last_activity != "contest":
                rest_days += 1
                last_activity = "contest"

    return rest_days

def main():
    # Read the number of days
    days = int(input())

    # Read the activities
    activities = list(map(int, input().split()))

    # Get the minimum number of rest days
    rest_days = get_min_rest_days(days, activities)

    # Print the result
    print(rest_days)

if __name__ == '__main__':
    main()

