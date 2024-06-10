
def get_subsequences(sequence):
    n = len(sequence)
    subsequences = [0] * (n + 1)
    subsequences[0] = 1
    for i in range(1, n + 1):
        subsequences[i] = subsequences[i - 1] * (i - 1)
    return subsequences

def count_subsequences(sequence, k):
    n = len(sequence)
    subsequences = get_subsequences(sequence)
    count = 0
    for i in range(n - k + 1):
        count += subsequences[k] - subsequences[i] * subsequences[n - i - k + 1]
    return count % 1000000007

def main():
    n = int(input())
    sequence = [int(x) for x in input().split()]
    for i in range(1, n + 1):
        print(count_subsequences(sequence, i))

if __name__ == '__main__':
    main()

