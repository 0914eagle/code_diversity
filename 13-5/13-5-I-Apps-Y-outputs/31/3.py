
import math

def get_angle(a, b, c, d):
    ab = [b[0] - a[0], b[1] - a[1], b[2] - a[2]]
    bc = [c[0] - b[0], c[1] - b[1], c[2] - b[2]]
    cd = [d[0] - c[0], d[1] - c[1], d[2] - c[2]]
    x = [ab[1] * bc[2] - ab[2] * bc[1], ab[2] * bc[0] - ab[0] * bc[2], ab[0] * bc[1] - ab[1] * bc[0]]
    y = [bc[1] * cd[2] - bc[2] * cd[1], bc[2] * cd[0] - bc[0] * cd[2], bc[0] * cd[1] - bc[1] * cd[0]]
    return math.degrees(math.acos((x[0] * y[0] + x[1] * y[1] + x[2] * y[2]) / (math.sqrt(x[0] ** 2 + x[1] ** 2 + x[2] ** 2) * math.sqrt(y[0] ** 2 + y[1] ** 2 + y[2] ** 2))))

