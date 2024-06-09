
def get_possible_pairs(numbers):
    n = len(numbers)
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] != numbers[j]:
                pairs += 1
    return pairs

