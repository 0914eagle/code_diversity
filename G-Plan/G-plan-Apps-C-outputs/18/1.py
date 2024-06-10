
def generate_sequences(input_seq):
    sequences = []
    if '?' not in input_seq:
        return [input_seq]
    else:
        idx = input_seq.index('?')
        for char in ['H', 'T']:
            new_seq = input_seq[:idx] + char + input_seq[idx+1:]
            sequences.extend(generate_sequences(new_seq))
    return sequences

def calculate_operations(seq):
    count_H = 0
    total_operations = 0
    for char in seq:
        if char == 'H':
            total_operations += count_H
            count_H += 1
        elif char == 'T':
            total_operations += count_H
    return total_operations

def average_operations(input_seq):
    sequences = generate_sequences(input_seq)
    total_operations = sum(calculate_operations(seq) for seq in sequences)
    return total_operations / len(sequences)

if __name__ == "__main__":
    input_seq = input().strip()
    result = average_operations(input_seq)
    print(result)
