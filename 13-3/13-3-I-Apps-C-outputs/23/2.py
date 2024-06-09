
def is_correct_sequence(sequence):
    stack = []
    for char in sequence:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

def reorder_sequence(sequence, start, end):
    subsequence = sequence[start:end+1]
    subsequence = subsequence[::-1]
    sequence = sequence[:start] + subsequence + sequence[end+1:]
    return sequence

def make_sequence_correct(sequence):
    if is_correct_sequence(sequence):
        return 0
    
    n = len(sequence)
    for i in range(n):
        for j in range(i+1, n+1):
            subsequence = sequence[i:j]
            if len(subsequence) % 2 == 0:
                continue
            reordered_sequence = reorder_sequence(sequence, i, j-1)
            if is_correct_sequence(reordered_sequence):
                return j - i
    
    return -1

n = int(input())
sequence = input()
print(make_sequence_correct(sequence))

