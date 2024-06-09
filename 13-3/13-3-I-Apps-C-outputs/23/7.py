
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
    
    # Find the first incorrect character
    for i in range(len(sequence)):
        if sequence[i] != "(" and sequence[i] != ")":
            break
    
    # Find the first correct character after the incorrect character
    for j in range(i+1, len(sequence)):
        if sequence[j] == "(" or sequence[j] == ")":
            break
    
    # Swap the characters at positions i and j
    sequence = sequence[:i] + sequence[j] + sequence[i+1:j] + sequence[i] + sequence[j+1:]
    
    # Recursively call the function to get the minimum time for the new sequence
    return 1 + get_min_time(sequence)

def main():
    n = int(input())
    sequence = input()
    print(get_min_time(sequence))

if __name__ == "__main__":
    main()

