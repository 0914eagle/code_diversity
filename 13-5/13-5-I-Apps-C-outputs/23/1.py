
def get_lis_length(sequence):
    # Implement your LIS algorithm here
    # You can use a dynamic programming approach or any other method you prefer
    pass

def get_critical_elements(sequence):
    lis_length = get_lis_length(sequence)
    critical_elements = []
    for i in range(len(sequence)):
        if get_lis_length(sequence[:i] + sequence[i+1:]) < lis_length:
            critical_elements.append(sequence[i])
    if not critical_elements:
        critical_elements = [-1]
    return critical_elements

if __name__ == '__main__':
    n = int(input())
    sequence = list(map(int, input().split()))
    print(*get_critical_elements(sequence), sep='\n')

