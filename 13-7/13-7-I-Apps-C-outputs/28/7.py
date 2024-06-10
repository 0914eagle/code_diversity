
def get_confused_pairs(sequence):
    confused_pairs = 0
    for i in range(len(sequence) - 1):
        for j in range(i + 1, len(sequence)):
            if sequence[i] > sequence[j]:
                confused_pairs += 1
    return confused_pairs

def count_sequences(N, C):
    sequences = 0
    for i in range(1, N + 1):
        sequence = list(range(1, N + 1))
        sequence[i - 1] = sequence[i]
        sequence[i] = sequence[i - 1]
        if get_confused_pairs(sequence) == C:
            sequences += 1
    return sequences

if __name__ == '__main__':
    N, C = map(int, input().split())
    print(count_sequences(N, C) % 1000000007)

