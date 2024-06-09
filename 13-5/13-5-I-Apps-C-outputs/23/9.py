
def get_lis_length(sequence):
    # Implement your solution here
    return len(sequence)

def get_critical_elements(sequence):
    # Find the longest increasing subsequence (LIS) of the sequence
    lis = []
    for i in range(len(sequence)):
        if not lis or sequence[i] > lis[-1]:
            lis.append(sequence[i])

    # Find the critical elements in the LIS
    critical_elements = []
    for i in range(len(lis)):
        if lis[i] != sequence[i]:
            critical_elements.append(sequence[i])

    return critical_elements

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    critical_elements = get_critical_elements(sequence)
    if critical_elements:
        print(*critical_elements)
    else:
        print(-1)

if __name__ == '__main__':
    main()

