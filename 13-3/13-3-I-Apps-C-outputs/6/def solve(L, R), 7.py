
def solve(L, R):
    count = 0
    for i in range(L, R+1):
        if '4' not in str(i) and str(i).count('6') == str(i).count('8'):
            count += 1
    return count % 1000000007

