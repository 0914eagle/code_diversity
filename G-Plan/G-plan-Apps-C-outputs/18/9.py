
def generate_sequences(input_seq):
    sequences = [input_seq]
    for i in range(len(input_seq)):
        if input_seq[i] == '?':
            new_sequences = []
            for seq in sequences:
                new_sequences.append(seq[:i] + 'H' + seq[i+1:])
                new_sequences.append(seq[:i] + 'T' + seq[i+1:])
            sequences = new_sequences
    return sequences

def calculate_operations(sequence):
    count_H = 0
    total_operations = 0
    for coin in sequence:
        if coin == 'H':
            count_H += 1
        else:
            total_operations += count_H
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
