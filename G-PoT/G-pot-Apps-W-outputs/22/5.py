
n = int(input())
for _ in range(n):
    s = input()
    t = input()
    
    if len(t) < len(s):
        print("NO")
    else:
        freq_s = {}
        freq_t = {}
        
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
        
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1
        
        valid = True
        for char, count in freq_t.items():
            if char not in freq_s or freq_s[char] < count:
                valid = False
                break
        
        if valid:
            print("YES")
        else:
            print("NO")
