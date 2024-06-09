
n, m, q = map(int, input().split())
s = input()
t = input()

for i in range(q):
    l, r = map(int, input().split())
    count = 0
    for j in range(l, r+1):
        if s[j:j+m] == t:
            count += 1
    print(count)

