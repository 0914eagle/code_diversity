
def calculate_level(n, k, s):
    level = 0
    current_char = s[0]
    char_count = 1
    for i in range(1, n):
        if s[i] == current_char:
            char_count += 1
        else:
            level = max(level, char_count // k)
            current_char = s[i]
            char_count = 1
    level = max(level, char_count // k)
    return level

if __name__ == "__main__":
    n, k = map(int, input().split())
    s = input().strip()
    print(calculate_level(n, k, s))
