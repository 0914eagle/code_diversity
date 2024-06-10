ulate_level(n, k, s):
    max_level = 0
    current_char = ''
    char_count = 0

    for i in range(n):
        if s[i] == current_char:
            char_count += 1
        else:
            max_level = max(max_level, char_count // k)
            current_char = s[i]
            char_count = 1

    max_level = max(max_level, char_count // k)
    return max_level

if __name__ == "__main__":
    n, k = map(int, input().split())
    s = input().strip()
    print(calculate_level(n, k, s))
