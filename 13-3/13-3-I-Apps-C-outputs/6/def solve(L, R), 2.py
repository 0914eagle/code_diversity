
def solve(L, R):
    count = 0
    for i in range(L, R+1):
        num = str(i)
        if '4' in num:
            continue
        sixes = eight = 0
        for digit in num:
            if digit == '6':
                sixes += 1
            elif digit == '8':
                eight += 1
        if sixes == eight:
            count += 1
    return count % 1000000007

