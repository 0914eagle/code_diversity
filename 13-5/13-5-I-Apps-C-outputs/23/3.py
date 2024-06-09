
def get_lis_length(sequence):
    # Find the longest increasing subsequence (LIS) length for the given sequence
    lis = [1] * len(sequence)
    for i in range(1, len(sequence)):
        for j in range(i):
            if sequence[i] > sequence[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis)

def get_critical_elements(sequence):
    # Find all the critical elements in the sequence
    lis = get_lis_length(sequence)
    critical_elements = []
    for i in range(len(sequence)):
        if lis == 1:
            break
        if sequence[i] not in critical_elements:
            critical_elements.append(sequence[i])
            lis -= 1
    if not critical_elements:
        critical_elements = [-1]
    return critical_elements

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    print(*get_critical_elements(sequence), sep='\n')

if __name__ == '__main__':
    main()

