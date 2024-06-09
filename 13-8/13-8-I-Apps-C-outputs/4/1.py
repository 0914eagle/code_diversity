
def solve(n, arr):
    # Initialize variables
    rest_days = 0
    gym_open = False
    contest_carried_out = False

    # Iterate through the array
    for i in range(n):
        # Check if the gym is open on this day
        if arr[i] == 2 or arr[i] == 3:
            gym_open = True

        # Check if the contest is carried out on this day
        if arr[i] == 1 or arr[i] == 3:
            contest_carried_out = True

        # Check if Vasya has a rest on this day
        if not gym_open and not contest_carried_out:
            rest_days += 1

        # Check if Vasya has done sport and written the contest on two consecutive days
        if gym_open and contest_carried_out and i > 0 and arr[i-1] in [2, 3]:
            rest_days += 1

        # Update the variables for the next day
        gym_open = False
        contest_carried_out = False

    return rest_days

