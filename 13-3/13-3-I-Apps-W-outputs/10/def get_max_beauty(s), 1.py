
def get_max_beauty(s):
    n = len(s)
    beauty = 0
    l, r = 0, 0
    for i in range(n):
        for j in range(i+1, n):
            tmp = s[i] + s[j]
            if tmp == "()":
                beauty += 1
            elif tmp == ")(":
                beauty += 2
            elif tmp == "()(":
                beauty += 3
            elif tmp == "()":
                beauty += 4
    
    return beauty, l, r

