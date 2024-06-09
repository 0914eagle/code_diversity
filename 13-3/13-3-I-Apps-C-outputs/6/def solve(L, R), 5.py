
def solve(L, R):
    count = 0
    for i in range(L, R+1):
        str_i = str(i)
        if '4' in str_i:
            continue
        sixes = str_i.count('6')
        eights = str_i.count('8')
        if sixes == eights:
            count += 1
    return count % 1000000007

