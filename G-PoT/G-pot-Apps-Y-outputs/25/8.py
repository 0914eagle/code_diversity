
n = int(input())
strings = [input() for _ in range(n)]

def is_substring(a, b):
    return a in b

def can_reorder_strings(strings):
    for i in range(n):
        for j in range(i+1, n):
            if is_substring(strings[i], strings[j]) or is_substring(strings[j], strings[i]):
                continue
            else:
                return "NO"
    return "YES"

result = can_reorder_strings(strings)
if result == "NO":
    print("NO")
else:
    print("YES")
    for string in strings:
        print(string)
