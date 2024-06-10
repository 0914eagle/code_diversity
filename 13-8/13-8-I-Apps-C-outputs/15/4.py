
def is_sorted(sequence):
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            if sequence[i] > sequence[j]:
                return False
    return True

def get_unsorted_sequences(sequence):
    unsorted_sequences = []
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            for k in range(j+1, len(sequence)):
                unsorted_sequences.append([sequence[i], sequence[j], sequence[k]])
    return unsorted_sequences

def count_unsorted_sequences(sequence):
    unsorted_sequences = get_unsorted_sequences(sequence)
    count = 0
    for sequence in unsorted_sequences:
        if is_sorted(sequence):
            count += 1
    return count

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    print(count_unsorted_sequences(sequence) % (10**9 + 9))

if __name__ == '__main__':
    main()

