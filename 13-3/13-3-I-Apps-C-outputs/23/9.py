
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
    
    # Find the first incorrect character from the end
    for j in range(len(sequence) - 1, i - 1, -1):
        if sequence[j] != "(" and sequence[j] != ")":
            break
    
    # Reorder the substring
    substring = sequence[i:j+1]
    reordered_substring = "".join(reversed(substring))
    sequence = sequence[:i] + reordered_substring + sequence[j+1:]
    
    # Recursively call the function to check if the sequence is correct
    return 1 + get_min_time(sequence)

def main():
    n = int(input())
    sequence = input()
    print(get_min_time(sequence))

if __name__ == "__main__":
    main()

