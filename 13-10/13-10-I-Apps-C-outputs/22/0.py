
def solve(base, num):
    for i in range(1, num+1):
        if int(str(i) * len(str(i))) == num:
            return i
    return "impossible"

