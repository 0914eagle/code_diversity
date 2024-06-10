
def get_subsequences(sequence, k):
    n = len(sequence)
    if k == 0:
        return 1
    if k == 1:
        return n
    if k > n:
        return 0
    return (get_subsequences(sequence, k-1) + get_subsequences(sequence, k-2)) % (10**9+7)

def count_subsequences(sequence):
    n = len(sequence)
    result = []
    for k in range(1, n+1):
        result.append(get_subsequences(sequence, k))
    return result

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    result = count_subsequences(sequence)
    for i in result:
        print(i)

if __name__ == '__main__':
    main()

