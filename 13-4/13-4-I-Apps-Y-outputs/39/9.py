
def get_sequences():
    k = int(input())
    sequences = []
    for i in range(k):
        n = int(input())
        sequence = list(map(int, input().split()))
        sequences.append(sequence)
    return sequences

def find_matching_sequences(sequences):
    for i in range(len(sequences)):
        for j in range(i+1, len(sequences)):
            if sequences[i] == sequences[j]:
                return i+1, j+1
    return -1, -1

def main():
    sequences = get_sequences()
    i, j = find_matching_sequences(sequences)
    if i == -1 and j == -1:
        print("NO")
    else:
        print("YES")
        print(i, j)

if __name__ == '__main__':
    main()

