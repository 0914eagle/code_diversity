
def get_lis_length(sequence):
    # Implement your solution here
    return len(sequence)

def get_critical_elements(sequence):
    # Find all critical elements in the sequence
    critical_elements = []
    for i in range(len(sequence)):
        # Check if removing the current element will decrease the LIS length
        current_element = sequence[i]
        remaining_sequence = sequence[:i] + sequence[i+1:]
        lis_length = get_lis_length(remaining_sequence)
        if lis_length < get_lis_length(sequence):
            critical_elements.append(current_element)
    return critical_elements

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    critical_elements = get_critical_elements(sequence)
    if len(critical_elements) == 0:
        print(-1)
    else:
        print(*critical_elements)

if __name__ == '__main__':
    main()

