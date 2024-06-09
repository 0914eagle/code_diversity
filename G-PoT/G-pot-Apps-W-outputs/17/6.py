
def determine_lines(n, d, w, inscription):
    words = []
    for line in inscription:
        words.extend(line.split('.'))
    
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
inscription = [input() for _ in range(n)]

# Call the function and print the output
print(determine_lines(n, d, w, inscription))
