
def get_number_of_pairs(numbers):
    n = len(numbers)
    pairs = set()
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] != numbers[j]:
                pairs.add((numbers[i], numbers[j]))
    return len(pairs)

