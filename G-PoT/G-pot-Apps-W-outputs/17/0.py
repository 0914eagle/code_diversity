
def determine_lines_needed(n, d, w, inscription):
    words = inscription.replace('.', ' ').split()
    lines = 1
    current_line_length = 0
    
    for word in words:
        if current_line_length + len(word) <= w:
            current_line_length += len(word) + 1
        else:
            lines += 1
            current_line_length = len(word) + 1
    
    return lines

# Read input
n, d, w = map(int, input().split())
inscription = ""
for _ in range(n):
    inscription += input()

# Call the function and print the output
print(determine_lines_needed(n, d, w, inscription))
