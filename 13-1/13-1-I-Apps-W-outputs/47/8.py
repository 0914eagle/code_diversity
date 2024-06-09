
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

    # If the input array has only one element, it cannot be solved
    if n == 1:
        return False

    # If the input array has two elements, it can be solved if they are equal
    if n == 2:
        return a[0] == a[1]

    # If the input array has three elements, it can be solved if the first two elements are equal and the last element is equal to the sum of the first two elements
    if n == 3:
        return a[0] == a[1] and a[1] + a[2] == a[0] + a[1]

    # If the input array has four elements, it can be solved if the first three elements are equal and the last element is equal to the sum of the first three elements
    if n == 4:
        return a[0] == a[1] == a[2] and a[0] + a[1] + a[2] == a[3]

    # If the input array has more than four elements, it cannot be solved
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

    # If the input array has only one element, it cannot be solved
    if n == 1:
        return []

    # If the input array has two elements, it can be solved if they are equal
    if n == 2:
        if a[0] == a[1]:
            return [a[0]]
        else:
            return []

    # If the input array has three elements, it can be solved if the first two elements are equal and the last element is equal to the sum of the first two elements
    if n == 3:
        if a[0] == a[1] and a[1] + a[2] == a[0] + a[1]:
            return [a[0]]
        else:
            return []

    # If the input array has four elements, it can be solved if the first three elements are equal and the last element is equal to the sum of the first three elements
    if n == 4:
        if a[0] == a[1] == a[2] and a[0] + a[1] + a[2] == a[3]:
            return [a[0]]
        else:
            return []

    # If the input array has more than four elements, it cannot be solved
    return []

n = int(input())
a = list(map(int, input().split()))

if is_solvable(n, a):
    print("YES")
    print(*find_missing_candies(n, a))
else:
    print("NO")

