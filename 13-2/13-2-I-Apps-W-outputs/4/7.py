
def restore_sequence(n, l_list, r_list):
    # Initialize an empty sequence
    sequence = []

    # Loop through each opening bracket
    for i in range(n):
        # Find the corresponding closing bracket
        for j in range(i+1, n):
            if l_list[i] <= j-i <= r_list[i]:
                sequence.append(')')
                break
        else:
            sequence.append('(')

    # Check if the sequence is correct
    if sequence[0] == '(' and sequence[-1] == ')':
        for i in range(1, n-1):
            if sequence[i] == '(' and sequence[i+1] == ')':
                return ''.join(sequence)

    return "IMPOSSIBLE"

