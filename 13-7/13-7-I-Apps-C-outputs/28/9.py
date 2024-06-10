
def get_confused_pairs(sequence):
    confused_pairs = 0
    for i in range(len(sequence) - 1):
        for j in range(i + 1, len(sequence)):
            if sequence[i] > sequence[j]:
                confused_pairs += 1
    return confused_pairs

def get_sequences_with_confusion(N, C):
    sequences = []
    for i in range(1, N + 1):
        sequence = [i]
        if get_confused_pairs(sequence) == C:
            sequences.append(sequence)
    return sequences

def main():
    N, C = map(int, input().split())
    print(get_sequences_with_confusion(N, C) % 1000000007)

if __name__ == '__main__':
    main()

