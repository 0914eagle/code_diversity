
def count_entirely_unsorted_sequences(sequence):
    n = len(sequence)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if sequence[i] > sequence[j]:
                count += 1
    return count

def count_permutations(sequence):
    n = len(sequence)
    permutations = 1
    for i in range(n):
        permutations *= n - i
    return permutations

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    count = count_entirely_unsorted_sequences(sequence)
    permutations = count_permutations(sequence)
    print(count * permutations % (10**9 + 9))

if __name__ == '__main__':
    main()

