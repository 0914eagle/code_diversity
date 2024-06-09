
def get_returnable_rooms(n, conveyor_belts):
    returnable_rooms = 0
    for i in range(n):
        if conveyor_belts[i] == '-' or conveyor_belts[(i+1)%n] == '-':
            returnable_rooms += 1
    return returnable_rooms

