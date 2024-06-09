
def frequency_sorter(sequence, max_value):
    frequency = [0] * (max_value + 1)
    for num in sequence:
        frequency[num] += 1
    sorted_sequence = []
    for i in range(max_value + 1):
        for j in range(frequency[i]):
            sorted_sequence.append(i)
    return sorted_sequence

