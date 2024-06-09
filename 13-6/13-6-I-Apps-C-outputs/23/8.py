
def get_sequence_length(sequence):
    n = len(sequence)
    count = 0
    for i in range(n):
        if sequence[i] == "H":
            count += 1
        if count > 0 and (i == n-1 or sequence[i+1] == "H"):
            count = 0
        if count == 0:
            break
    return count

def get_average_sequence_length(sequence):
    n = len(sequence)
    total_length = 0
    for i in range(n):
        sub_sequence = sequence[i:n]
        total_length += get_sequence_length(sub_sequence)
    return total_length / n

if __name__ == '__main__':
    sequence = input()
    print(get_average_sequence_length(sequence))

