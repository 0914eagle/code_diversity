
n = int(input())
arr = list(map(int, input().split()))

# Initialize variables to keep track of the number of days Vasya has rest
rest_days = 0

# Iterate through the list of days
for i in range(n):
    # If the gym is closed and the contest is not carried out, Vasya has a rest
    if arr[i] == 0:
        rest_days += 1
    # If the gym is open and the contest is carried out, Vasya has a rest
    elif arr[i] == 3:
        rest_days += 1
    # If the gym is open and the contest is not carried out, Vasya does sport
    elif arr[i] == 2:
        # If the next day is also open and the contest is not carried out, Vasya has a rest
        if i < n-1 and arr[i+1] == 2:
            rest_days += 1
        # If the next day is closed or the contest is carried out, Vasya does sport
        else:
            pass
    # If the gym is closed and the contest is carried out, Vasya does sport
    elif arr[i] == 1:
        # If the next day is also closed and the contest is carried out, Vasya has a rest
        if i < n-1 and arr[i+1] == 1:
            rest_days += 1
        # If the next day is open and the contest is not carried out, Vasya does sport
        elif i < n-1 and arr[i+1] == 2:
            pass
        # If the next day is closed or the contest is carried out, Vasya does sport
        else:
            pass

print(rest_days)

