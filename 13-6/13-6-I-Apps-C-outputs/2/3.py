
def solve(L, R):
    count = 0
    for num in range(L, R+1):
        if '4' in str(num):
            continue
        sixes = len([d for d in str(num) if d == '6'])
        eights = len([d for d in str(num) if d == '8'])
        if sixes == eights:
            count += 1
    return count % 1000000007

