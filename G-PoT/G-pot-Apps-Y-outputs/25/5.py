
n = int(input())
strings = [input() for _ in range(n)]

def is_substring(s1, s2):
    return s1 in s2

strings.sort(key=len)
for i in range(n):
    for j in range(i+1, n):
        if not is_substring(strings[i], strings[j]):
            print("NO")
            break
    else:
        continue
    break
else:
    print("YES")
    for s in strings:
        print(s)
