
def solve(sequence, k):
    # Sort the sequence in ascending order
    sequence.sort()

    # Initialize the left and right boundaries of the binary search
    left = 1
    right = 10**9

    # Perform binary search to find the smallest number that satisfies the condition
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for num in sequence:
            if num <= mid:
                count += 1
        if count == k:
            return mid
        elif count < k:
            left = mid + 1
        else:
            right = mid - 1

    # If no such number is found, return -1
    return -1

