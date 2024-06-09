
def solve(L, R):
    count = 0
    for num in range(L, R+1):
        num_str = str(num)
        if '4' in num_str:
            continue
        count_6 = num_str.count('6')
        count_8 = num_str.count('8')
        if count_6 == count_8:
            count += 1
    return count % 1000000007

