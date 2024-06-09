
n = int(input())
s = input()

count_eights = s.count('8')

if count_eights > n // 2:
    print("YES")
else:
    print("NO")
