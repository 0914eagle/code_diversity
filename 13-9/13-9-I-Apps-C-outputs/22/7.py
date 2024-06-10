
def solve(a00, a01, a10, a11):
    if a00 + a01 + a10 + a11 == 0:
        return "Impossible"
    
    # initialize variables
    s = ""
    i = 0
    j = 0
    k = 0
    l = 0
    
    # iterate through all possible strings of length 2
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    # check if the current string matches the given integers
                    if (i == 0 and j == 0 and k == 1 and l == 1) or (i == 0 and j == 1 and k == 0 and l == 1) or (i == 1 and j == 0 and k == 1 and l == 0) or (i == 1 and j == 1 and k == 0 and l == 0):
                        s += "01"
                    elif (i == 0 and j == 0 and k == 1 and l == 0) or (i == 0 and j == 1 and k == 0 and l == 1) or (i == 1 and j == 0 and k == 1 and l == 1) or (i == 1 and j == 1 and k == 0 and l == 0):
                        s += "10"
                    else:
                        s += "00"
    
    # check if the current string matches the given integers
    if a00 == s.count("00") and a01 == s.count("01") and a10 == s.count("10") and a11 == s.count("11"):
        return s
    else:
        return "Impossible"

if __name__ == '__main__':
    a00, a01, a10, a11 = map(int, input().split())
    print(solve(a00, a01, a10, a11))

