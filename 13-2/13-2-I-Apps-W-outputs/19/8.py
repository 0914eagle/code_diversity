
def is_adjacent(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == '-' and s[i+1] == '-':
            count += 1
    return count

def is_valid(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == '-' and s[i+1] == 'o':
            count += 1
    return count % 2 == 0

def can_rejoin(s):
    if len(s) == 1:
        return "YES"
    if is_adjacent(s) == 0:
        return "NO"
    if is_valid(s):
        return "YES"
    for i in range(len(s)):
        if s[i] == '-':
            s = s[:i] + 'o' + s[i+1:]
            if can_rejoin(s) == "YES":
                return "YES"
    return "NO"

s = input()
print(can_rejoin(s))

