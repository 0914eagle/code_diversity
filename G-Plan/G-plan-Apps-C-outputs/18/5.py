
def generate_sequences(input_seq):
    sequences = []
    question_marks = input_seq.count('?')
    for i in range(2 ** question_marks):
        seq = list(input_seq)
        for j, char in enumerate(seq):
            if char == '?':
                if i % 2 == 0:
                    seq[j] = 'H'
                else:
                    seq[j] = 'T'
                i //= 2
        sequences.append(''.join(seq))
    return sequences

def calculate_operations(sequence):
    count_h = 0
    total_operations = 0
    for char in sequence:
        if char == 'H':
            count_h += 1
        else:
            total_operations += count_h
    return total_operations

def calculate_average_operations(input_seq):
    sequences = generate_sequences(input_seq)
    total_operations = sum(calculate_operations(seq) for seq in sequences)
    average_operations = total_operations / len(sequences)
    return average_operations

if __name__ == "__main__":
    input_seq = input().strip()
    result = calculate_average_operations(input_seq)
    print(result)
