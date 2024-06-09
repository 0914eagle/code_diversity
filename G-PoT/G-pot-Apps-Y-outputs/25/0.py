
n = int(input())
strings = []
for _ in range(n):
    strings.append(input())

strings.sort(key=len)  # Sort strings by length

for i in range(n):
    for j in range(i+1, n):
        if strings[i] not in strings[j]:
            print("NO")
            break
    else:
        continue
    break
else:
    print("YES")
    for string in strings:
        print(string)
