
def get_maximum(sequence):
    result = []
    for i in range(len(sequence)):
        max_value = 0
        for j in range(len(sequence)):
            if j != i and sequence[j] > max_value:
                max_value = sequence[j]
        result.append(max_value)
    return result

