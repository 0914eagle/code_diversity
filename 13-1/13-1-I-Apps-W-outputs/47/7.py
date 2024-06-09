
def is_possible(n, a):
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

    # If the input array has two elements, it is not possible to find the missing number of candies
    if n == 2:
        return False

    # If the input array has three elements, it is possible to find the missing number of candies
    if n == 3:
        return True

    # If the input array has four elements, it is possible to find the missing number of candies
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

    # If the input array has two elements, it is not possible to find the missing number of candies
    if n == 2:
        return []

    # If the input array has three elements, it is possible to find the missing number of candies
    if n == 3:
        return [mean]

    # If the input array has four elements, it is possible to find the missing number of candies
    if n == 4:
        return [mean - a[0], mean - a[1], mean - a[2], mean - a[3]]

    # If the input array has more than four elements, it is not possible to find the missing number of candies
    return []

n = int(input())
a = list(map(int, input().split()))

if is_possible(n, a):
    print("YES")
    print(*find_missing_candies(n, a))
else:
    print("NO")

