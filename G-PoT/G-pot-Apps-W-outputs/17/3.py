
n, d, w = map(int, input().split())
lines = [input() for _ in range(n)]

total_lines = 0
for line in lines:
    words = line.split('.')
    current_line = ''
    for word in words:
        if len(current_line) + len(word) <= w:
            current_line += word
        else:
            total_lines += 1
            current_line = word
    if current_line:
        total_lines += 1

print(total_lines)
