
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
        # If Vasya has a rest on the previous day, he can do sport on this day
        if rest_days > 0:
            rest_days -= 1
        # If Vasya does not have a rest on the previous day, he can do sport on this day
        else:
            rest_days = 0

# Print the minimum number of days Vasya has rest
print(rest_days)

