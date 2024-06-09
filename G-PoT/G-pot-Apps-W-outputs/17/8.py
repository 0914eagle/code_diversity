
n, d, w = map(int, input().split())
lines = [input() for _ in range(n)]

def calculate_lines(lines, w):
    current_line = ""
    total_lines = 0
    for line in lines:
        words = line.split('.')
        for word in words:
            if len(current_line) + len(word) <= w:
                current_line += word
            else:
                total_lines += 1
                current_line = word
        if current_line:
            total_lines += 1
            current_line = ""
    return total_lines

result = calculate_lines(lines, w)
print(result)
