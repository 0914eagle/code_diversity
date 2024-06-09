
def determine_lines(n, d, w, inscription):
    words = inscription.split('.')
    lines = 0
    current_line = ''
    
    for word in words:
        if len(current_line) + len(word) <= w:
            current_line += word
        else:
            lines += 1
            current_line = word
    
    if current_line:
        lines += 1
    
    return lines

# Read input
n, d, w = map(int, input().split())
inscription = ''
for _ in range(n):
    line = input()
    inscription += line.replace(' ', '.')

# Determine number of lines needed
result = determine_lines(n, d, w, inscription)
print(result)
