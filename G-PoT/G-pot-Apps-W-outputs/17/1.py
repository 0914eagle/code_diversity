
def determine_lines(n, d, w, inscription):
    words = []
    for line in inscription:
        words.extend(line.split('.'))
    
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= w:
            if current_line:
                current_line += "."
            current_line += word
        else:
            lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    return len(lines)

# Read input
n, d, w = map(int, input().split())
inscription = [input() for _ in range(n)]

# Call the function and print the output
print(determine_lines(n, d, w, inscription))
