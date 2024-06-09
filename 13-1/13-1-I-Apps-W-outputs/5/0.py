
def get_shortest_correct_sequence(S):
    # Initialize variables
    N = len(S)
    open_brackets = 0
    close_brackets = 0
    sequence = []

    # Iterate through the string S
    for i in range(N):
        # If the current character is an open bracket, increment the number of open brackets
        if S[i] == '(':
            open_brackets += 1
        # If the current character is a close bracket, increment the number of close brackets
        elif S[i] == ')':
            close_brackets += 1
        # If the number of open brackets is greater than the number of close brackets, insert an open bracket into the sequence
        if open_brackets > close_brackets:
            sequence.append('(')
        # If the number of close brackets is greater than the number of open brackets, insert a close bracket into the sequence
        elif close_brackets > open_brackets:
            sequence.append(')')
    
    # Return the lexicographically smallest string among the shortest correct bracket sequences
    return ''.join(sequence)

if __name__ == '__main__':
    N = int(input())
    S = input()
    print(get_shortest_correct_sequence(S))

