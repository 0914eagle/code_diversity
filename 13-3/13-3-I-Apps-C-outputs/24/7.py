
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

def get_min_time(sequence):
    if is_correct_sequence(sequence):
        return 0
    
    n = len(sequence)
    min_time = float("inf")
    for i in range(n):
        for j in range(i+1, n+1):
            sub_sequence = sequence[i:j]
            reordered_sub_sequence = "".join(reversed(sub_sequence))
            time = len(sub_sequence)
            new_sequence = sequence[:i] + reordered_sub_sequence + sequence[j:]
            min_time = min(min_time, time + get_min_time(new_sequence))
    
    return min_time

def main():
    n = int(input())
    sequence = input()
    print(get_min_time(sequence))

if __name__ == '__main__':
    main()

