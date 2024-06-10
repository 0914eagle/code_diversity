
def get_input():
    return map(int, input().split())

def get_substring_count(s, c1, c2):
    count = 0
    for i in range(len(s) - 1):
        if s[i] == c1 and s[i + 1] == c2:
            count += 1
    return count

def solve():
    a00, a01, a10, a11 = get_input()
    if a00 + a01 + a10 + a11 == 0:
        return "Impossible"
    s = "0" * a00 + "1" * a10
    if get_substring_count(s, "0", "1") == a01:
        return s
    s = "1" * a11 + "0" * a01
    if get_substring_count(s, "1", "0") == a10:
        return s
    return "Impossible"

if __name__ == '__main__':
    print(solve())

