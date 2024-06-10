
def get_subsequences(sequence):
    n = len(sequence)
    subsequences = [0] * (n + 1)
    subsequences[0] = 1
    for i in range(1, n + 1):
        subsequences[i] = (subsequences[i - 1] * (n - i + 1)) % 1000000007
    return subsequences

def count_subsequences(sequence, k):
    n = len(sequence)
    subsequences = get_subsequences(sequence)
    return (subsequences[k] * subsequences[n - k]) % 1000000007

if __name__ == '__main__':
    n = int(input())
    sequence = list(map(int, input().split()))
    for i in range(1, n + 1):
        print(count_subsequences(sequence, i))

