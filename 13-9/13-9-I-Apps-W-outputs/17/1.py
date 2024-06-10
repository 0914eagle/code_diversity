
def read_input():
    n = int(input())
    sequence = list(map(int, input().split()))
    return n, sequence

def get_subsequence_count(sequence, k):
    n = len(sequence)
    count = 0
    for i in range(n - k + 1):
        subsequence = sequence[i:i+k]
        if len(set(subsequence)) == k:
            count += 1
    return count % 1000000007

def main():
    n, sequence = read_input()
    for k in range(1, n+1):
        print(get_subsequence_count(sequence, k))

if __name__ == '__main__':
    main()

