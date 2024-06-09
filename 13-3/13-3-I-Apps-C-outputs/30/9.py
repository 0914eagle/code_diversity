
def is_quadrilateral(p1, p2, p3, p4):
    return (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p4[1] + p4[0] * p1[1]) - (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p4[0] + p4[1] * p1[0]) != 0

def is_inside_or_on_border(p, q1, q2, q3, q4):
    return is_quadrilateral(p, q1, q2, q3) and is_quadrilateral(p, q1, q2, q4) and is_quadrilateral(p, q1, q3, q4) and is_quadrilateral(p, q2, q3, q4)

def count_dangerous_castles(nazis, castles):
    dangerous_castles = 0
    for castle in castles:
        for nazi in nazis:
            if is_inside_or_on_border(nazi, castle, (castle[0] + 1, castle[1]), (castle[0], castle[1] + 1), (castle[0] + 1, castle[1] + 1)):
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

