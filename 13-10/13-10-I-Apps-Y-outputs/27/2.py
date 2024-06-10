
def is_duplicate_pair(s):
    count = 0
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                count += 1
    return count == 2

def solve(s):
    if len(s) != 4:
        return "No"
    if not s.isupper() or len(set(s)) != 4:
        return "No"
    count = 0
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                count += 1
    if count == 2:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    s = input()
    print(solve(s))

