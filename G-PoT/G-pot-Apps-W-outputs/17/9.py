
def calculate_lines(n, d, w, inscription):
    words = inscription.split('.')
    lines = 1
    current_line_length = 0
    
    for word in words:
        if len(word) + current_line_length <= w:
            current_line_length += len(word)
        else:
            lines += 1
            current_line_length = len(word)
    
    return lines

# Read input
n, d, w = map(int, input().split())
inscription = ""
for _ in range(n):
    line = input().strip()
    inscription += line.replace(' ', '.')

# Calculate number of lines required
result = calculate_lines(n, d, w, inscription)
print(result)
