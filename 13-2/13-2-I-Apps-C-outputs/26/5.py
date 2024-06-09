
def f1(n, current_sequence, fossil_sequences):
    # Initialize variables
    first_path_sequences = []
    second_path_sequences = []
    first_path_count = 0
    second_path_count = 0

    # Iterate through the fossil sequences
    for sequence in fossil_sequences:
        # Check if the sequence is in the genetic history of the current species
        if sequence in current_sequence:
            # If it is, add it to the first path
            first_path_sequences.append(sequence)
            first_path_count += 1
        else:
            # If it's not, add it to the second path
            second_path_sequences.append(sequence)
            second_path_count += 1

    # Return the number of sequences in each path and the sequences themselves
    return first_path_count, first_path_sequences, second_path_count, second_path_sequences

def f2(n, current_sequence, fossil_sequences):
    # Initialize variables
    first_path_sequences = []
    second_path_sequences = []
    first_path_count = 0
    second_path_count = 0

    # Iterate through the fossil sequences
    for sequence in fossil_sequences:
        # Check if the sequence is in the genetic history of the current species
        if sequence in current_sequence:
            # If it is, add it to the first path
            first_path_sequences.append(sequence)
            first_path_count += 1
        else:
            # If it's not, add it to the second path
            second_path_sequences.append(sequence)
            second_path_count += 1

    # Return the number of sequences in each path and the sequences themselves
    return first_path_count, first_path_sequences, second_path_count, second_path_sequences

if __name__ == '__main__':
    n = int(input())
    current_sequence = input()
    fossil_sequences = []
    for i in range(n):
        fossil_sequences.append(input())
    first_path_count, first_path_sequences, second_path_count, second_path_sequences = f1(n, current_sequence, fossil_sequences)
    print(first_path_count, second_path_count)
    for sequence in first_path_sequences:
        print(sequence)
    for sequence in second_path_sequences:
        print(sequence)

