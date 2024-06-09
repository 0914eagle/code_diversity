
s = input().strip()
result = ''
for i in range(1, len(s)+1, 2):
    result += s[i-1]
print(result)
