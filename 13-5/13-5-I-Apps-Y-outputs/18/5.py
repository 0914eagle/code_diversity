
def find_available_room(r, n, booked_rooms):
    available_rooms = [i for i in range(1, r+1) if i not in booked_rooms]
    if available_rooms:
        return available_rooms[0]
    else:
        return "too late"

