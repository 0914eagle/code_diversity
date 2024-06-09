
def f1(n, m, s):
    # Initialize variables
    witch_cells = set()
    treasure_cell = (n, m)
    current_cell = (1, 1)
    visited_cells = set([current_cell])
    queue = [(1, 1)]

    # Breadth-first search to find the shortest path from (1, 1) to (n, m)
    while queue:
        current_cell = queue.pop(0)
        if current_cell == treasure_cell:
            break
        for next_cell in [(current_cell[0] + 1, current_cell[1]), (current_cell[0], current_cell[1] + 1)]:
            if next_cell[0] <= n and next_cell[1] <= m and next_cell not in visited_cells and next_cell not in witch_cells and s[next_cell[0] - 1][next_cell[1] - 1] == ".":
                queue.append(next_cell)
                visited_cells.add(next_cell)

    # Return the minimum number of cells the witch needs to turn into impassable forests
    return len(visited_cells) - 1

def f2(n, m, s):
    # Initialize variables
    witch_cells = set()
    treasure_cell = (n, m)
    current_cell = (1, 1)
    visited_cells = set([current_cell])
    queue = [(1, 1)]

    # Breadth-first search to find the shortest path from (1, 1) to (n, m)
    while queue:
        current_cell = queue.pop(0)
        if current_cell == treasure_cell:
            break
        for next_cell in [(current_cell[0] + 1, current_cell[1]), (current_cell[0], current_cell[1] + 1)]:
            if next_cell[0] <= n and next_cell[1] <= m and next_cell not in visited_cells and next_cell not in witch_cells and s[next_cell[0] - 1][next_cell[1] - 1] == ".":
                queue.append(next_cell)
                visited_cells.add(next_cell)

    # Return the minimum number of cells the witch needs to turn into impassable forests
    return len(visited_cells) - 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    print(f1(n, m, s))
    print(f2(n, m, s))

