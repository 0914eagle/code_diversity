
import sys

def get_confused_pairs(sequence):
    confused_pairs = 0
    for i in range(len(sequence) - 1):
        for j in range(i + 1, len(sequence)):
            if sequence[i] > sequence[j]:
                confused_pairs += 1
    return confused_pairs

def count_sequences(n, c):
    sequences = 0
    for i in range(1, n + 1):
        sequence = list(range(1, n + 1))
        sequence.remove(i)
        confused_pairs = get_confused_pairs(sequence)
        if confused_pairs == c:
            sequences += 1
    return sequences

n, c = map(int, sys.stdin.readline().split())
print(count_sequences(n, c) % 1000000007)

