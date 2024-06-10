
def get_subsequences(sequence, length):
    subsequences = []
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            subsequences.append(sequence[i:j+1])
    return subsequences

def count_subsequences(sequence, length):
    subsequences = get_subsequences(sequence, length)
    unique_subsequences = set(map(tuple, subsequences))
    return len(unique_subsequences) % (10**9 + 7)

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    for i in range(1, n+1):
        print(count_subsequences(sequence, i))

if __name__ == '__main__':
    main()

