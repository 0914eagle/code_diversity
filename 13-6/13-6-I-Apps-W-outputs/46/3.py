
def solve(n, a):
    # Initialize the result variable
    result = 0

    # Loop through the array and check if the marbles are in order
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            # If the marbles are not in order, find the leftmost and rightmost marbles of the same color
            left = i
            right = i + 1
            while left >= 0 and a[left] == a[i]:
                left -= 1
            while right < n and a[right] == a[i]:
                right += 1

            # Swap the leftmost and rightmost marbles of the same color
            a[left], a[right] = a[right], a[left]
            result += 1

    return result

