
def solve(L, R):
    count = 0
    for i in range(L, R+1):
        num_str = str(i)
        if '4' in num_str:
            continue
        num_6 = num_str.count('6')
        num_8 = num_str.count('8')
        if num_6 == num_8:
            count += 1
    return count % 1000000007

