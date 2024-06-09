
def is_safe_order(rooms):
    
    # Initialize the pile with the exams from the first room
    pile = rooms[0]
    # Visit each room in order
    for i in range(1, len(rooms)):
        # Take exams from the top of the pile and distribute them to the students in the current room
        current_room = rooms[i]
        # If the pile contains at least as many exams as there are students in the current room, we can safely visit the current room
        if len(pile) >= current_room:
            # Distribute the exams from the pile to the students in the current room
            pile = pile[current_room:]
        # If the pile contains fewer exams than there are students in the current room, we cannot safely visit the current room
        else:
            return False
    return True

def find_safe_order(rooms):
    
    # Try all possible orders
    for order in permutations(rooms):
        if is_safe_order(order):
            return order
    return None

def main():
    n = int(input())
    rooms = [int(input()) for _ in range(n)]
    safe_order = find_safe_order(rooms)
    if safe_order is None:
        print("impossible")
    else:
        print(" ".join(map(str, safe_order)))

if __name__ == "__main__":
    main()

