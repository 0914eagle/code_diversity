
def is_solution_possible(n, a):
    # Sort the input array in non-decreasing order
    a.sort()
    
    # Calculate the arithmetic mean, median, and range of the input array
    mean = sum(a) / n
    median = a[n // 2]
    range = a[n - 1] - a[0]
    
    # Check if the mean, median, and range are equal
    if mean == median == range:
        return True
    else:
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
        # If they are equal, return the missing candies as the difference between the mean and each element in the array
        return [int(mean - x) for x in a]
    else:
        # If they are not equal, return an empty list
        return []

n = int(input())
a = list(map(int, input().split()))

if is_solution_possible(n, a):
    print("YES")
    print(*find_missing_candies(n, a))
else:
    print("NO")

