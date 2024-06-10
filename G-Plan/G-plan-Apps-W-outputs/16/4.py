
def calculate_level(n, k, s):
    level = 0
    current_char = s[0]
    char_count = 1
    max_level = 0

    for i in range(1, n):
        if s[i] == current_char:
            char_count += 1
        else:
            level = char_count // k
            max_level = max(max_level, level)
            current_char = s[i]
            char_count = 1

    level = char_count // k
    max_level = max(max_level, level)

    return max_level

if __name__ == "__main__":
    n, k = map(int, input().split())
    s = input().strip()
    print(calculate_level(n, k, s))
