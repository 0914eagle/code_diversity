
n = int(input())
for _ in range(n):
    s = input()
    t = input()
    
    s_index = 0
    t_index = 0
    valid = True
    
    while s_index < len(s) and t_index < len(t):
        if s[s_index] != t[t_index]:
            valid = False
            break
        s_count = 1
        t_count = 1
        
        while s_index + s_count < len(s) and s[s_index + s_count] == s[s_index]:
            s_count += 1
        while t_index + t_count < len(t) and t[t_index + t_count] == t[t_index]:
            t_count += 1
        
        if t_count < s_count:
            valid = False
            break
        
        s_index += s_count
        t_index += t_count
    
    if s_index != len(s) or t_index != len(t):
        valid = False
    
    if valid:
        print("YES")
    else:
        print("NO")
