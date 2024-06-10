
def read_input():
    N, C = map(int, input().split())
    return N, C

def generate_sequences(N, C):
    sequences = []
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            for k in range(j+1, N+1):
                if i < j and j < k:
                    sequences.append((i, j, k))
    return sequences

def count_confused_pairs(sequence):
    confused_pairs = 0
    for i in range(len(sequence)-1):
        for j in range(i+1, len(sequence)):
            if sequence[i] > sequence[j]:
                confused_pairs += 1
    return confused_pairs

def count_sequences(N, C):
    sequences = generate_sequences(N, C)
    count = 0
    for sequence in sequences:
        if count_confused_pairs(sequence) == C:
            count += 1
    return count

def main():
    N, C = read_input()
    print(count_sequences(N, C) % 1000000007)

if __name__ == '__main__':
    main()

