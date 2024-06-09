
def f1(n, k):
    # find the kth valid sequence
    valid_sequences = []
    for i in range(1, n):
        for j in range(1, n):
            if i*j % n != 0:
                valid_sequences.append([i, j])
    return valid_sequences[k-1]

def f2(n, k):
    # find the kth valid sequence using lexicographic ordering
    valid_sequences = []
    for i in range(1, n):
        for j in range(1, n):
            if i*j % n != 0:
                valid_sequences.append([i, j])
    valid_sequences.sort()
    return valid_sequences[k-1]

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    print(f1(n, k))
    print(f2(n, k))

