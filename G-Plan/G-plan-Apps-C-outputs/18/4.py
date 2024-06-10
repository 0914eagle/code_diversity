
def generate_sequences(sequence):
    sequences = [sequence]
    index = sequence.find('?')
    while index != -1:
        new_sequences = []
        for seq in sequences:
            new_sequences.append(seq[:index] + 'H' + seq[index+1:])
            new_sequences.append(seq[:index] + 'T' + seq[index+1:])
        sequences = new_sequences
        index = sequences[0].find('?')
    return sequences

def calculate_operations(sequence):
    count_H = 0
    total_operations = 0
    for char in sequence:
        if char == 'H':
            count_H += 1
            total_operations += count_H
        elif char == 'T':
            total_operations += count_H
    return total_operations / len(sequence)

def solve_problem(input_sequence):
    sequences = generate_sequences(input_sequence)
    total_avg_operations = sum(calculate_operations(seq) for seq in sequences) / len(sequences)
    return total_avg_operations

if __name__ == "__main__":
    input_sequence = input().strip()
    result = solve_problem(input_sequence)
    print(result)
