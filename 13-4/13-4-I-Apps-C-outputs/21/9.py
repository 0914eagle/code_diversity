
def solve(numbers):
    n = len(numbers) // 2
    sums = [0] * n
    for i in range(n):
        sums[i] = round(numbers[i]) + round(numbers[i + n])
    return abs(sum(sums))

