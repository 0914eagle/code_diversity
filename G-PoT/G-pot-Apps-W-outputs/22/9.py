
n = int(input())
for _ in range(n):
    s = input()
    t = input()
    
    if len(s) > len(t):
        print("NO")
    else:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        if i == len(s):
            print("YES")
        else:
            print("NO")
