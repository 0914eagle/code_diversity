
import itertools

def count_confused_sequences(N, C):
    # Initialize a list to store the number of confused pairs for each sequence
    confused_pairs = [0] * (N + 1)
    # Initialize a list to store the number of sequences with each number of confused pairs
    sequences = [0] * (C + 1)
    # Initialize a list to store the number of sequences with each number of confused pairs and each number of elements
    sequences_with_N_elements = [[0] * (N + 1) for _ in range(C + 1)]

    # Iterate over all possible sequences of length N
    for numbers in itertools.permutations(range(1, N + 1)):
        # Count the number of confused pairs in the current sequence
        current_confused_pairs = 0
        for i in range(N - 1):
            if numbers[i] > numbers[i + 1]:
                current_confused_pairs += 1
        # Add the current sequence to the list of sequences with the current number of confused pairs
        sequences_with_N_elements[current_confused_pairs][N] += 1
        # Add the current sequence to the list of sequences with the current number of elements
        sequences_with_N_elements[current_confused_pairs][numbers[0]] += 1
        # Add the current sequence to the list of sequences with the current number of confused pairs
        sequences[current_confused_pairs] += 1
        # Add the current sequence to the list of sequences with the current number of confused pairs and the current number of elements
        confused_pairs[current_confused_pairs] += 1

    # Return the number of sequences with the given number of confused pairs
    return sequences[C]

def main():
    N, C = map(int, input().split())
    print(count_confused_sequences(N, C))

if __name__ == "__main__":
    main()

