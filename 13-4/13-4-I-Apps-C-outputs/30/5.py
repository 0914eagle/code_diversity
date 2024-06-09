
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
    
    # Find the longest substring of balanced parentheses
    longest_substring = 0
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)+1):
            substring = sequence[i:j]
            if is_correct_sequence(substring):
                longest_substring = max(longest_substring, len(substring))
    
    # Reorder the substring
    reordered_substring = sequence[:longest_substring]
    for i in range(longest_substring):
        reordered_substring = reordered_substring[1:] + reordered_substring[0]
    
    # Recursively call the function on the reordered substring
    return 1 + get_min_time(reordered_substring)

def main():
    n = int(input())
    sequence = input()
    print(get_min_time(sequence))

if __name__ == "__main__":
    main()

