
def solve(map1, map2):
    # Find the length of the common section
    n = len(map1)
    m = len(map1[0])
    for i in range(n-m+1):
        for j in range(m-m+1):
            if map1[i:i+m] == map2[j:j+m]:
                return i+1, j+1
    return -1, -1

