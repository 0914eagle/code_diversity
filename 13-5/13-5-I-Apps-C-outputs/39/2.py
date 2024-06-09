
def solve(L, R):
    count = 0
    for i in range(L, R+1):
        str_i = str(i)
        if '4' in str_i:
            continue
        count_6 = str_i.count('6')
        count_8 = str_i.count('8')
        if count_6 == count_8:
            count += 1
    return count % 1000000007

