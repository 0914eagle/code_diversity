
def count_pairs(numbers):
    n = len(numbers)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] != numbers[j]:
                count += 1
    return count

