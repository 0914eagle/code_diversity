
n = int(input())
for _ in range(n):
    s = input()
    t = input()
    
    s_ptr = 0
    t_ptr = 0
    while s_ptr < len(s) and t_ptr < len(t):
        if s[s_ptr] != t[t_ptr]:
            print("NO")
            break
        s_count = 1
        t_count = 1
        while s_ptr + s_count < len(s) and s[s_ptr + s_count] == s[s_ptr]:
            s_count += 1
        while t_ptr + t_count < len(t) and t[t_ptr + t_count] == t[t_ptr]:
            t_count += 1
        if t_count < s_count:
            print("NO")
            break
        s_ptr += s_count
        t_ptr += t_count
    else:
        if s_ptr == len(s) and t_ptr == len(t):
            print("YES")
        else:
            print("NO")
