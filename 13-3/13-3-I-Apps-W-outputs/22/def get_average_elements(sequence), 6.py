
def get_average_elements(sequence):
    average_elements = 0
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            if sequence[i] == (sequence[j] + sequence[i]) // 2:
                average_elements += 1
                break
    return average_elements

