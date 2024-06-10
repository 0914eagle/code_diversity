
def calculate_level(n, k, s):
    max_level = 0
    current_level = 0
    current_char = ''
    current_char_count = 0

    for char in s:
        if char == current_char:
            current_char_count += 1
        else:
            current_level += current_char_count // k
            max_level = max(max_level, current_level)
            current_char = char
            current_char_count = 1
            current_level = 1

    current_level += current_char_count // k
    max_level = max(max_level, current_level)

    return max_level

if __name__ == "__main__":
    n, k = map(int, input().split())
    s = input().strip()
    print(calculate_level(n, k, s))
