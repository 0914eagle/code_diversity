
def generate_sequences(sequence):
    sequences = [sequence]
    for i, char in enumerate(sequence):
        if char == '?':
            new_sequences = []
            for seq in sequences:
                new_sequences.append(seq[:i] + 'H' + seq[i+1:])
                new_sequences.append(seq[:i] + 'T' + seq[i+1:])
            sequences = new_sequences
    return sequences

def calculate_operations(sequence):
    count_H = 0
    total_operations = 0
    for char in sequence:
        if char == 'H':
            count_H += 1
            total_operations += count_H
        else:
            count_H = 0
    return total_operations

def average_operations(sequence):
    sequences = generate_sequences(sequence)
    total_operations = sum(calculate_operations(seq) for seq in sequences)
    return total_operations / len(sequences)

if __name__ == "__main__":
    input_sequence = input().strip()
    print(average_operations(input_sequence))
