
def get_min_rest_days(n, a):
    # Initialize variables
    rest_days = 0
    gym_open = False
    contest_held = False

    # Iterate through the input array
    for i in range(n):
        # Check if the gym is open and a contest is held on the current day
        if a[i] == 0:
            gym_open = False
            contest_held = False
        elif a[i] == 1:
            gym_open = False
            contest_held = True
        elif a[i] == 2:
            gym_open = True
            contest_held = False
        else:
            gym_open = True
            contest_held = True

        # Check if Vasya has a rest on the current day
        if not gym_open and not contest_held:
            rest_days += 1

        # Check if Vasya has a rest on the previous day
        if i > 0 and (not gym_open or not contest_held) and (a[i-1] == 0 or a[i-1] == 2):
            rest_days += 1

    return rest_days

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_min_rest_days(n, a))

if __name__ == '__main__':
    main()

