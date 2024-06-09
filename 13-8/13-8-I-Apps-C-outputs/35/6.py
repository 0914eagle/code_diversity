
def get_returnable_rooms(n, conveyor_belts):
    returnable_rooms = 0
    for i in range(n):
        if conveyor_belts[i] == "<" and conveyor_belts[(i+1)%n] == ">":
            returnable_rooms += 1
        elif conveyor_belts[i] == ">" and conveyor_belts[(i+1)%n] == "<":
            returnable_rooms += 1
        elif conveyor_belts[i] == "-":
            returnable_rooms += 2
    return returnable_rooms

