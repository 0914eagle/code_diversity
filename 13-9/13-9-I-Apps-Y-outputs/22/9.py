
def solve(N, s):
    max_grade = 0
    for i in range(N):
        max_grade += s[i]
        if max_grade % 10 == 0:
            max_grade -= 1
    return max_grade

