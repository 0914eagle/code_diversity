
def get_dangerous_castles(nazis, castles):
    dangerous_castles = 0
    for castle in castles:
        is_dangerous = False
        for i in range(len(nazis)):
            for j in range(i+1, len(nazis)):
                if (nazis[i][0] == nazis[j][0] and nazis[i][1] == nazis[j][1]) or (castle[0] == nazis[i][0] and castle[1] == nazis[i][1]) or (castle[0] == nazis[j][0] and castle[1] == nazis[j][1]):
                    continue
                if (nazis[i][0] == castle[0] and nazis[i][1] == castle[1]) or (nazis[j][0] == castle[0] and nazis[j][1] == castle[1]):
                    is_dangerous = True
                    break
            if is_dangerous:
                break
        if is_dangerous:
            dangerous_castles += 1
    return dangerous_castles

