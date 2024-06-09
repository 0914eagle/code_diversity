
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

def get_correct_sequence(sequence):
    if is_correct_sequence(sequence):
        return sequence
    
    stack = []
    for i in range(len(sequence)):
        char = sequence[i]
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return -1
            stack.pop()
    
    if not stack:
        return sequence
    
    while stack:
        sequence = sequence[:i] + sequence[i:]
        i = (i - 1) % len(sequence)
    
    return sequence

def get_time_to_make_correct(sequence):
    correct_sequence = get_correct_sequence(sequence)
    if correct_sequence == -1:
        return -1
    
    time = 0
    for i in range(len(sequence)):
        if sequence[i] != correct_sequence[i]:
            time += 1
    
    return time

def main():
    n = int(input())
    sequence = input()
    print(get_time_to_make_correct(sequence))

if __name__ == '__main__':
    main()

