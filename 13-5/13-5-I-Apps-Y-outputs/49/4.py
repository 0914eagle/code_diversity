
def max_operations(numbers):
    count = 0
    while all(n % 2 == 0 for n in numbers):
        numbers = [n // 2 for n in numbers]
        count += 1
    return count

