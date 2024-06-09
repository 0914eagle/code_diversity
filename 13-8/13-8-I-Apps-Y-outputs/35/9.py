
def get_balanced_ternary_string(s):
    n = len(s)
    count = [s.count(i) for i in "012"]
    diff = max(count) - min(count)
    if diff > 1:
        return "Impossible"
    
    ans = []
    for i in range(n):
        if s[i] == "0":
            if count[0] > count[1]:
                ans.append("1")
                count[1] += 1
            else:
                ans.append("2")
                count[2] += 1
        elif s[i] == "1":
            if count[1] > count[2]:
                ans.append("2")
                count[2] += 1
            else:
                ans.append("0")
                count[0] += 1
        else:
            if count[2] > count[0]:
                ans.append("0")
                count[0] += 1
            else:
                ans.append("1")
                count[1] += 1
    
    return "".join(ans)

