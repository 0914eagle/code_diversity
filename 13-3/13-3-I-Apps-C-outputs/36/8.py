
def get_dangerous_castles(nazis, castles):
    dangerous_castles = 0
    for castle in castles:
        # Check if the castle is inside or on the border of a non-degenerate quadrilateral formed by four Nazi troops
        inside_quadrilateral = False
        for i in range(nazis):
            for j in range(i+1, len(nazis)):
                for k in range(j+1, len(nazis)):
                    if (nazis[i][0] == nazis[j][0] and nazis[j][0] == nazis[k][0]) or (nazis[i][1] == nazis[j][1] and nazis[j][1] == nazis[k][1]):
                        continue
                    if (nazis[i][0] * nazis[j][1] + nazis[j][0] * nazis[k][1] + nazis[k][0] * nazis[i][1]) == (nazis[i][1] * nazis[j][0] + nazis[j][1] * nazis[k][0] + nazis[k][1] * nazis[i][0]):
                        continue
                    if (nazis[i][0] * castle[1] + nazis[j][0] * castle[1] + nazis[k][0] * castle[1]) == (nazis[i][1] * castle[0] + nazis[j][1] * castle[0] + nazis[k][1] * castle[0]):
                        inside_quadrilateral = True
                        break
        if inside_quadrilateral:
            dangerous_castles += 1
    return dangerous_castles

