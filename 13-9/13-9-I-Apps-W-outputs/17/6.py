
def get_subsequences(sequence):
    n = len(sequence)
    subsequences = [0] * (n + 1)
    subsequences[0] = 1
    for i in range(1, n + 1):
        subsequences[i] = (subsequences[i - 1] * 2) % 1000000007
    for i in range(1, n + 1):
        for j in range(i):
            if sequence[i - 1] != sequence[j]:
                subsequences[i] = (subsequences[i] + subsequences[j]) % 1000000007
    return subsequences

def solve(n, sequence):
    subsequences = get_subsequences(sequence)
    result = []
    for i in range(1, n + 1):
        result.append(subsequences[i])
    return result

if __name__ == '__main__':
    n = int(input())
    sequence = list(map(int, input().split()))
    result = solve(n, sequence)
    for i in result:
        print(i)

