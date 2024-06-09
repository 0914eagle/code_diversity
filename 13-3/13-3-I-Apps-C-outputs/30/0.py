
def is_quadrilateral(p1, p2, p3, p4):
    return (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p4[1] + p4[0] * p1[1]) - (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p4[0] + p4[1] * p1[0]) != 0

def is_inside_or_on_border(p, castle):
    x, y = p
    x1, y1 = castle
    x2, y2 = castle[1:]
    return (x1 <= x <= x2 and y1 <= y <= y2) or (x1 >= x >= x2 and y1 >= y >= y2) or (x1 <= x <= x2 and y1 >= y >= y2) or (x1 >= x >= x2 and y1 <= y <= y2)

def count_dangerous_castles(nazis, castles):
    dangerous_castles = 0
    for castle in castles:
        for i in range(len(nazis)):
            for j in range(i+1, len(nazis)):
                for k in range(j+1, len(nazis)):
                    if is_quadrilateral(nazis[i], nazis[j], nazis[k], castle) and is_inside_or_on_border(castle, castle):
                        dangerous_castles += 1
                        break
    return dangerous_castles

if __name__ == '__main__':
    nazis = []
    castles = []
    for _ in range(int(input())):
        nazis.append(tuple(map(int, input().split())))
    for _ in range(int(input())):
        castles.append(tuple(map(int, input().split())))
    print(count_dangerous_castles(nazis, castles))

