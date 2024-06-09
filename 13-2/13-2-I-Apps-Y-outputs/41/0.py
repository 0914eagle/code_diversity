
def is_safe_order(rooms):
    # Initialize a pile of exams with the number of exams in the first room
    pile = rooms[0]
    # Iterate through the remaining rooms
    for i in range(1, len(rooms)):
        # If the pile has enough exams to distribute to the current room, distribute them and add the exams from the current room to the pile
        if pile >= rooms[i]:
            pile += rooms[i]
        # If the pile does not have enough exams to distribute to the current room, return False
        else:
            return False
    return True

def get_safe_order(rooms):
    # Initialize a list to store the safe order
    safe_order = []
    # Iterate through the rooms
    for i in range(len(rooms)):
        # If the current room is safe to visit, add it to the safe order
        if is_safe_order(rooms[i:]):
            safe_order.append(i)
    # If no safe order exists, return "impossible"
    if not safe_order:
        return "impossible"
    # Otherwise, return the safe order
    return safe_order

n = int(input())
rooms = [int(i) for i in input().split()]
print(get_safe_order(rooms))

