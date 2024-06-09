
def solve(L, R):
    count = 0
    for i in range(L, R+1):
        num_digits = len(str(i))
        num_6s = sum(int(c) == 6 for c in str(i))
        num_8s = sum(int(c) == 8 for c in str(i))
        if "4" not in str(i) and num_6s == num_8s:
            count += 1
    return count % 1000000007

