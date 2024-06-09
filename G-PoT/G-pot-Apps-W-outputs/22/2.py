
n = int(input())
for _ in range(n):
    s = input()
    t = input()
    
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            print("NO")
            break
        count_s = 1
        count_t = 1
        while i+1 < len(s) and s[i] == s[i+1]:
            count_s += 1
            i += 1
        while j+1 < len(t) and t[j] == t[j+1]:
            count_t += 1
            j += 1
        if count_t < count_s:
            print("NO")
            break
        i += 1
        j += 1
    else:
        if i == len(s) and j == len(t):
            print("YES")
        else:
            print("NO")
