
def is_quadrilateral(p1, p2, p3, p4):
    return (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p4[1] + p4[0] * p1[1]) - (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p4[0] + p4[1] * p1[0]) != 0

def is_inside_quadrilateral(p, p1, p2, p3, p4):
    return (p[0] - p1[0]) * (p2[1] - p1[1]) + (p1[0] - p2[0]) * (p[1] - p1[1]) >= 0 and (p[0] - p2[0]) * (p3[1] - p2[1]) + (p2[0] - p3[0]) * (p[1] - p2[1]) >= 0 and (p[0] - p3[0]) * (p4[1] - p3[1]) + (p3[0] - p4[0]) * (p[1] - p3[1]) >= 0 and (p[0] - p4[0]) * (p1[1] - p4[1]) + (p4[0] - p1[0]) * (p[1] - p4[1]) >= 0

def count_dangerous_castles(nazis, castles):
    dangerous_castles = 0
    for castle in castles:
        for i in range(len(nazis)):
            for j in range(i+1, len(nazis)):
                for k in range(j+1, len(nazis)):
                    if is_quadrilateral(nazis[i], nazis[j], nazis[k], castle) and is_inside_quadrilateral(castle, nazis[i], nazis[j], nazis[k], castle):
                        dangerous_castles += 1
                        break
    return dangerous_castles

if __name__ == '__main__':
    nazis = []
    castles = []
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        nazis.append((x, y))
    m = int(input())
    for i in range(m):
        x, y = map(int, input().split())
        castles.append((x, y))
    print(count_dangerous_castles(nazis, castles))

