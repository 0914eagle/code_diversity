
def solve(numbers):
    n = len(numbers)
    if n == 1:
        return "YES"
    for i in range(n):
        left = (i - 1) % n
        right = (i + 1) % n
        if numbers[i] >= numbers[left] + numbers[right]:
            return "NO"
    return "YES"

