
def shortest_time_to_reach_beaver_den(map):
    # Initialize variables
    rows, cols = len(map), len(map[0])
    start_row, start_col = None, None
    dest_row, dest_col = None, None
    time = 0
    visited = set()
    queue = []

    # Find the starting point and destination
    for row in range(rows):
        for col in range(cols):
            if map[row][col] == "S":
                start_row, start_col = row, col
            elif map[row][col] == "D":
                dest_row, dest_col = row, col

    # Breadth-first search
    queue.append((start_row, start_col, time))
    visited.add((start_row, start_col))
    while queue:
        row, col, time = queue.pop(0)

        # If we have reached the destination, return the time
        if row == dest_row and col == dest_col:
            return time

        # Check all possible moves
        for new_row, new_col in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= new_row < rows and 0 <= new_col < cols and map[new_row][new_col] != "X" and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, time+1))
                visited.add((new_row, new_col))

    # If we reach this point, it means we couldn't find a path to the destination
    return "KAKTUS"

def main():
    map = [
        [".", "*", "."],
        [".", ".", "."],
        ["S", ".", "."]
    ]
    print(shortest_time_to_reach_beaver_den(map))

if __name__ == '__main__':
    main()

