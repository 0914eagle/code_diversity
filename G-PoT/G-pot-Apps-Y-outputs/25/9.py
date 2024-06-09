
n = int(input())
strings = [input() for _ in range(n)]

def is_substring(s1, s2):
    return s1 in s2

def can_reorder_strings(strings):
    strings.sort(key=len)  # Sort strings by length
    for i in range(1, len(strings)):
        if not is_substring(strings[i-1], strings[i]):
            return "NO"
    return "YES"

result = can_reorder_strings(strings)
if result == "YES":
    print(result)
    for s in strings:
        print(s)
else:
    print(result)
