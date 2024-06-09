
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
        sequence = sequence[:i] + "()" + sequence[i:]
        stack.pop()
    
    return sequence

def main():
    n = int(input())
    sequence = input()
    print(get_correct_sequence(sequence))

if __name__ == '__main__':
    main()

