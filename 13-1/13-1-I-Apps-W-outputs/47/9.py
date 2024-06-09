
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

    # If the input array has only one element, it is not possible to find a solution
    if n == 1:
        return False

    # If the input array has two elements, it is possible to find a solution if the two elements are equal
    if n == 2:
        if a[0] == a[1]:
            return True
        else:
            return False

    # If the input array has three elements, it is possible to find a solution if the three elements are equal
    if n == 3:
        if a[0] == a[1] == a[2]:
            return True
        else:
            return False

    # If the input array has four elements, it is possible to find a solution if the four elements are equal
    if n == 4:
        if a[0] == a[1] == a[2] == a[3]:
            return True
        else:
            return False

    # If the input array has more than four elements, it is not possible to find a solution
    return False

def find_solution(n, a):
    # Sort the input array in non-decreasing order
    a.sort()

    # Calculate the arithmetic mean, median, and range of the input array
    mean = sum(a) / n
    median = a[n // 2]
    range = a[n - 1] - a[0]

    # Check if the mean, median, and range are equal
    if mean == median == range:
        return a

    # If the input array has only one element, it is not possible to find a solution
    if n == 1:
        return []

    # If the input array has two elements, it is possible to find a solution if the two elements are equal
    if n == 2:
        if a[0] == a[1]:
            return [a[0]]
        else:
            return []

    # If the input array has three elements, it is possible to find a solution if the three elements are equal
    if n == 3:
        if a[0] == a[1] == a[2]:
            return [a[0]]
        else:
            return []

    # If the input array has four elements, it is possible to find a solution if the four elements are equal
    if n == 4:
        if a[0] == a[1] == a[2] == a[3]:
            return [a[0]]
        else:
            return []

    # If the input array has more than four elements, it is not possible to find a solution
    return []

n = int(input())
a = list(map(int, input().split()))

if is_solvable(n, a):
    print("YES")
    for b in find_solution(n, a):
        print(b)
else:
    print("NO")

