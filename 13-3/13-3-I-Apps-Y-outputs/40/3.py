
def get_max_values(sequence):
    max_values = []
    for i in range(len(sequence)):
        max_value = 0
        for j in range(len(sequence)):
            if j != i and sequence[j] > max_value:
                max_value = sequence[j]
        max_values.append(max_value)
    return max_values

