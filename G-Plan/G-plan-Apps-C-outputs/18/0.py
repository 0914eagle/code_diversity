
def generate_sequences(input_seq):
    sequences = [input_seq]
    for i, char in enumerate(input_seq):
        if char == '?':
            new_sequences = []
            for seq in sequences:
                new_sequences.append(seq[:i] + 'H' + seq[i+1:])
                new_sequences.append(seq[:i] + 'T' + seq[i+1:])
            sequences = new_sequences
    return sequences

def calculate_operations(seq):
    count_H = 0
    total_operations = 0
    for char in seq:
        if char == 'H':
            count_H += 1
        else:
            total_operations += count_H
    return total_operations

def average_operations(input_seq):
    sequences = generate_sequences(input_seq)
    total_operations = sum(calculate_operations(seq) for seq in sequences)
    return total_operations / len(sequences)

if __name__ == "__main__":
    input_seq = input().strip()
    print(average_operations(input_seq))
