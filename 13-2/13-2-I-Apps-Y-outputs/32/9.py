
def can_reach_destination(start, end, battery):
    # Initialize a queue to store the paths
    queue = [[start]]
    visited = set()

    # Loop until the queue is empty
    while queue:
        # Get the current path from the queue
        path = queue.pop(0)
        current = path[-1]

        # If the current coordinate is the destination, return True
        if current == end:
            return True

        # If the current coordinate is already visited, skip it
        if current in visited:
            continue

        # Mark the current coordinate as visited
        visited.add(current)

        # Get the available moves from the current coordinate
        moves = get_available_moves(current)

        # Loop through the available moves
        for move in moves:
            # If the move is valid and the battery has enough charge, add the move to the queue
            if move_is_valid(move, battery) and battery >= move[2]:
                queue.append(path + [move])
                battery -= move[2]

    # If the queue is empty and the battery is not empty, return False
    return False

def get_available_moves(coordinate):
    # Get the available moves from the current coordinate
    moves = [(coordinate[0], coordinate[1] + 1, 1), (coordinate[0], coordinate[1] - 1, 1), (coordinate[0] + 1, coordinate[1], 1), (coordinate[0] - 1, coordinate[1], 1)]
    return moves

def move_is_valid(move, battery):
    # Check if the move is valid
    if move[0] < -1000 or move[0] > 1000 or move[1] < -1000 or move[1] > 1000:
        return False
    if move[2] > battery:
        return False
    return True

def main():
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    battery = int(input())
    print("Y" if can_reach_destination(start, end, battery) else "N")

if __name__ == "__main__":
    main()

