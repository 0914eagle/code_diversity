
def is_solvable(n, a):
    # Sort the input array in non-decreasing order
    a.sort()
    # Initialize the mean, median, and range variables
    mean, median, range = 0, 0, 0
    # Loop through the input array
    for i in range(n):
        # Calculate the mean, median, and range
        mean += a[i]
        median += a[i]
        range += a[i]
    mean /= n
    median /= n
    range = a[n - 1] - a[0]
    # Check if the mean, median, and range are equal
    if mean == median == range:
        # If they are equal, return "YES"
        return "YES"
    else:
        # If they are not equal, return "NO"
        return "NO"

def find_missing_candies(n, a):
    # Sort the input array in non-decreasing order
    a.sort()
    # Initialize the mean, median, and range variables
    mean, median, range = 0, 0, 0
    # Loop through the input array
    for i in range(n):
        # Calculate the mean, median, and range
        mean += a[i]
        median += a[i]
        range += a[i]
    mean /= n
    median /= n
    range = a[n - 1] - a[0]
    # Check if the mean, median, and range are equal
    if mean == median == range:
        # If they are equal, return the missing candies
        return [int(mean)] * (4 - n)
    else:
        # If they are not equal, return an empty list
        return []

n = int(input())
a = list(map(int, input().split()))
print(is_solvable(n, a))
print(*find_missing_candies(n, a))

