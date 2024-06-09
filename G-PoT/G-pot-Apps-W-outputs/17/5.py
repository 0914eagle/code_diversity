
def calculate_lines(n, d, w, inscription):
    lines = 1
    current_line = 0
    current_length = 0
    
    for i in range(n):
        words = inscription[i].split('.')
        for word in words:
            if current_length + len(word) <= w:
                current_length += len(word)
            else:
                lines += 1
                current_length = len(word)
            current_length += 1  # for the period between words
        
    return lines

# Read input
n, d, w = map(int, input().split())
inscription = [input() for _ in range(n)]

# Calculate number of lines required
result = calculate_lines(n, d, w, inscription)
print(result)
