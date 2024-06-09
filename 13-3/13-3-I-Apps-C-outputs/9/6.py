
import sys

def get_confused_pairs(seq):
    confused_pairs = 0
    for i in range(len(seq) - 1):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                confused_pairs += 1
    return confused_pairs

def count_sequences(n, c):
    sequences = 0
    for i in range(1, n + 1):
        seq = list(range(1, n + 1))
        seq.remove(i)
        confused_pairs = get_confused_pairs(seq)
        if confused_pairs == c:
            sequences += 1
    return sequences

n, c = map(int, sys.stdin.readline().split())
print(count_sequences(n, c) % 1000000007)

