
def get_returnable_rooms(n, conveyor_belts):
    returnable_rooms = 0
    for i in range(n):
        if conveyor_belts[i] == "<":
            if i == 0:
                returnable_rooms += 1
            elif conveyor_belts[i-1] == ">":
                returnable_rooms += 1
        elif conveyor_belts[i] == ">":
            if i == n-1:
                returnable_rooms += 1
            elif conveyor_belts[i+1] == "<":
                returnable_rooms += 1
        else:
            returnable_rooms += 2
    return returnable_rooms

