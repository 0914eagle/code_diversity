
def solve(a, b):
    # Calculate the absolute difference between a and b
    diff = abs(a - b)

    # If the difference is odd, we can make it even by adding 1
    if diff % 2 == 1:
        return diff // 2 + 1

    # If the difference is even, we can make it odd by subtracting 1
    else:
        return diff // 2

