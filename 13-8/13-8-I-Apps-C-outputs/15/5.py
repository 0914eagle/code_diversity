
def get_entirely_unsorted_sequences(numbers):
    
    n = len(numbers)
    sorted_sequences = []
    for i in range(n):
        sorted_sequences.append([numbers[i]])
        for j in range(i+1, n):
            if numbers[j] < numbers[i]:
                sorted_sequences[i].append(numbers[j])
    unsorted_sequences = []
    for sequence in sorted_sequences:
        if len(sequence) == 1:
            unsorted_sequences.append(sequence)
        else:
            for i in range(len(sequence)):
                for j in range(i+1, len(sequence)):
                    if sequence[i] > sequence[j]:
                        unsorted_sequences.append(sequence[:i] + sequence[j:i:-1] + sequence[i+1:])
    return len(unsorted_sequences) % (10**9 + 9)

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(get_entirely_unsorted_sequences(numbers))

if __name__ == '__main__':
    main()

