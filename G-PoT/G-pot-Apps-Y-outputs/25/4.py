
n = int(input())
strings = [input() for _ in range(n)]

def is_substring(s1, s2):
    return s1 in s2

def can_reorder_strings(strings):
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_substring(strings[i], strings[j]):
                continue
            if is_substring(strings[j], strings[i]):
                return "NO"
    return "YES"

result = can_reorder_strings(strings)
if result == "YES":
    print(result)
    for string in strings:
        print(string)
else:
    print(result)
