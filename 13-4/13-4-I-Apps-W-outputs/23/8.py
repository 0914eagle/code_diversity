
def solve(a):
    if a == 0:
        return "yes"
    else:
        for i in range(1, a+1):
            if a % i == 0:
                return "yes"
        return "no"

