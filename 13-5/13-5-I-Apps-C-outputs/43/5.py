
def get_valid_sequences(n, k):
    valid_sequences = []
    for i in range(1, n):
        for j in range(1, n):
            if i * j % n != 0:
                valid_sequences.append([i, j])
    return valid_sequences[k - 1]

def get_kth_sequence(n, k):
    valid_sequences = get_valid_sequences(n, k)
    return " ".join(str(x) for x in valid_sequences)

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(get_kth_sequence(n, k))

