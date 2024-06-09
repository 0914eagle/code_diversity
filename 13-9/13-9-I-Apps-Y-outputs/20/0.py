
def solve(sides):
    s1, s2, s3, s4 = sides
    area = 0
    for i in range(1, 4):
        for j in range(i + 1, 5):
            k = (s1 * s2 + s2 * s3 + s3 * s4 + s1 * s4 - s2 * s3 - s3 * s4 - s1 * s4) / (s1 + s2 + s3 + s4)
            area = max(area, abs((s1 + s2 - k) * (s3 + s4 - k) * k))
    return area

