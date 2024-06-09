
def get_dangerous_castles(nazis, castles):
    dangerous_castles = set()
    for i in range(len(nazis)):
        for j in range(i+1, len(nazis)):
            for k in range(j+1, len(nazis)):
                for l in range(k+1, len(nazis)):
                    if is_quadrilateral(nazis[i], nazis[j], nazis[k], nazis[l]) and is_inside_or_on_border(nazis[i], nazis[j], nazis[k], nazis[l], castles):
                        dangerous_castles.add(castles[i])
    return len(dangerous_castles)

def is_quadrilateral(p1, p2, p3, p4):
    return not collinear(p1, p2, p3) and not collinear(p1, p2, p4) and not collinear(p2, p3, p4) and not collinear(p1, p3, p4)

def is_inside_or_on_border(p1, p2, p3, p4, castles):
    return any(is_inside_or_on_border_helper(p1, p2, p3, p4, castle) for castle in castles)

def is_inside_or_on_border_helper(p1, p2, p3, p4, castle):
    return (p1[0] <= castle[0] <= p2[0] or p1[0] >= castle[0] >= p2[0]) and (p1[1] <= castle[1] <= p2[1] or p1[1] >= castle[1] >= p2[1])

def collinear(p1, p2, p3):
    return p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]) == 0

if __name__ == '__main__':
    nazis = []
    castles = []
    for _ in range(int(input())):
        nazis.append(tuple(map(int, input().split())))
    for _ in range(int(input())):
        castles.append(tuple(map(int, input().split())))
    print(get_dangerous_castles(nazis, castles))

