
def solve(numbers):
    count = 0
    while all(num % 2 == 0 for num in numbers):
        count += 1
        numbers = [num // 2 for num in numbers]
    return count

