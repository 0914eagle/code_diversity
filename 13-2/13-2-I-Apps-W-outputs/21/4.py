
def solve(A, B):
    count = 0
    for a in range(1, A+1):
        for b in range(1, B+1):
            if str(a) not in str(b) and str(b) not in str(a) and a*b + a + b == int(str(a)+str(b)):
                count += 1
    return count

