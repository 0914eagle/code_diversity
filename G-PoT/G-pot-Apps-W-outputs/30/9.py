
n = int(input())
s = input()

count_8 = s.count('8')
if count_8 <= n // 2:
    print("YES")
else:
    print("NO")
