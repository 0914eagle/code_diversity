
def is_quadrilateral(x1, y1, x2, y2, x3, y3, x4, y4):
    return not (x1 == x2 or x1 == x3 or x1 == x4 or x2 == x3 or x2 == x4 or x3 == x4) and x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1 != x2 * y1 + x3 * y2 + x4 * y3 + x1 * y4

def get_dangerous_castles(nazis, castles):
    dangerous_castles = set()
    for i in range(len(nazis)):
        for j in range(i+1, len(nazis)):
            for k in range(j+1, len(nazis)):
                for l in range(k+1, len(nazis)):
                    if is_quadrilateral(nazis[i][0], nazis[i][1], nazis[j][0], nazis[j][1], nazis[k][0], nazis[k][1], nazis[l][0], nazis[l][1]):
                        for castle in castles:
                            if (castle[0] >= min(nazis[i][0], nazis[j][0], nazis[k][0], nazis[l][0]) and castle[0] <= max(nazis[i][0], nazis[j][0], nazis[k][0], nazis[l][0])) and (castle[1] >= min(nazis[i][1], nazis[j][1], nazis[k][1], nazis[l][1]) and castle[1] <= max(nazis[i][1], nazis[j][1], nazis[k][1], nazis[l][1]))):
                                dangerous_castles.add(castle)
    return len(dangerous_castles)

