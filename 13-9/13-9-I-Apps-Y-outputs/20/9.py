
def solve(sides):
    s1, s2, s3, s4 = sides
    max_area = 0
    for i in range(1, 4):
        for j in range(i+1, 4):
            for k in range(j+1, 4):
                l = 4 - i - j - k
                area = (s1 * s2 * s3 * s4) / (s[i] * s[j] * s[k] * s[l])
                max_area = max(max_area, area)
    return max_area

