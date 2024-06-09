
def solve(r, n, booked_rooms):
    available_rooms = list(set(range(1, r+1)) - set(booked_rooms))
    if available_rooms:
        return available_rooms[0]
    else:
        return "too late"

