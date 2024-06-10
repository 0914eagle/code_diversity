
def calculate_level(n, k, s):
    max_level = 0
    current_char = s[0]
    current_count = 1

    for i in range(1, n):
        if s[i] == current_char:
            current_count += 1
        else:
            max_level = max(max_level, current_count // k)
            current_char = s[i]
            current_count = 1

    max_level = max(max_level, current_count // k)
    return max_level

if __name__ == "__main__":
    n, k = map(int, input().split())
    s = input().strip()
    print(calculate_level(n, k, s))
