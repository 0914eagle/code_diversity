
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
    stack = []
    for char in sequence:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return "".join(stack)

def get_min_time(sequence):
    if is_correct_sequence(sequence):
        return 0
    correct_sequence = get_correct_sequence(sequence)
    if not correct_sequence:
        return -1
    time = 0
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)+1):
            sub_sequence = sequence[i:j]
            if is_correct_sequence(sub_sequence):
                time += len(sub_sequence)
                break
    return time

if __name__ == '__main__':
    n = int(input())
    sequence = input()
    print(get_min_time(sequence))

