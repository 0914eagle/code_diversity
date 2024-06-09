
def is_quadrilateral(p1, p2, p3, p4):
    return (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p4[1] + p4[0] * p1[1]) - (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p4[0] + p4[1] * p1[0]) != 0

def is_non_degenerate_quadrilateral(p1, p2, p3, p4):
    return is_quadrilateral(p1, p2, p3, p4) and not is_collinear(p1, p2, p3) and not is_collinear(p1, p2, p4) and not is_collinear(p2, p3, p4)

def is_collinear(p1, p2, p3):
    return p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]) == 0

def is_inside_or_on_border(p, quadrilateral):
    p1, p2, p3, p4 = quadrilateral
    return is_quadrilateral(p1, p2, p3, p) or is_quadrilateral(p1, p2, p4, p) or is_quadrilateral(p2, p3, p4, p) or is_quadrilateral(p1, p3, p4, p)

def count_in_danger_castles(nazis, castles):
    in_danger_castles = 0
    for castle in castles:
        for i in range(len(nazis)):
            for j in range(i+1, len(nazis)):
                for k in range(j+1, len(nazis)):
                    if is_non_degenerate_quadrilateral(nazis[i], nazis[j], nazis[k], castle) and is_inside_or_on_border(castle, (nazis[i], nazis[j], nazis[k], castle)):
                        in_danger_castles += 1
                        break
    return in_danger_castles

