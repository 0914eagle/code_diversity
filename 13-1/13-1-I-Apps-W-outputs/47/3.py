
def is_solvable(n, a):
    # Sort the input array in non-decreasing order
    a.sort()

    # Calculate the arithmetic mean, median, and range of the input array
    mean = sum(a) / n
    median = a[n // 2]
    range = a[n - 1] - a[0]

    # Check if the mean, median, and range are equal
    if mean == median == range:
        return True

    # If the input array has only one element, it is not possible to find the missing number of candies
    if n == 1:
        return False

    # If the input array has two elements, the missing number of candies can be found by calculating the difference between the two elements
    if n == 2:
        return True

    # If the input array has three elements, the missing number of candies can be found by calculating the difference between the two elements and the sum of the two elements
    if n == 3:
        return True

    # If the input array has four elements, the missing number of candies can be found by calculating the difference between the two elements and the sum of the two elements
    if n == 4:
        return True

    # If the input array has more than four elements, it is not possible to find the missing number of candies
    return False

def find_missing_candies(n, a):
    # Sort the input array in non-decreasing order
    a.sort()

    # Calculate the arithmetic mean, median, and range of the input array
    mean = sum(a) / n
    median = a[n // 2]
    range = a[n - 1] - a[0]

    # Check if the mean, median, and range are equal
    if mean == median == range:
        return []

    # If the input array has only one element, it is not possible to find the missing number of candies
    if n == 1:
        return []

    # If the input array has two elements, the missing number of candies can be found by calculating the difference between the two elements
    if n == 2:
        return [a[1] - a[0]]

    # If the input array has three elements, the missing number of candies can be found by calculating the difference between the two elements and the sum of the two elements
    if n == 3:
        return [a[1] - a[0], a[2] - a[1]]

    # If the input array has four elements, the missing number of candies can be found by calculating the difference between the two elements and the sum of the two elements
    if n == 4:
        return [a[1] - a[0], a[2] - a[1], a[3] - a[2]]

    # If the input array has more than four elements, it is not possible to find the missing number of candies
    return []

n = int(input())
a = list(map(int, input().split()))

if is_solvable(n, a):
    print("YES")
    for b in find_missing_candies(n, a):
        print(b)
else:
    print("NO")

