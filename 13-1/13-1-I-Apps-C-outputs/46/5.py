
def solve(n, m, k, o, c, graph):
    # Initialize a set to store the cells with iron ore
    iron_ore_cells = set()
    # Initialize a set to store the cells with coal
    coal_cells = set()
    # Initialize a set to store the claimed cells
    claimed_cells = set()
    # Initialize a variable to store the minimum number of settlers needed
    min_settlers = 0

    # Loop through the cells with iron ore
    for cell in o:
        # If the cell is not already claimed, claim it and add it to the set of claimed cells
        if cell not in claimed_cells:
            claimed_cells.add(cell)
            # Add the cell to the set of cells with iron ore
            iron_ore_cells.add(cell)
            # Increment the minimum number of settlers needed
            min_settlers += 1

    # Loop through the cells with coal
    for cell in c:
        # If the cell is not already claimed, claim it and add it to the set of claimed cells
        if cell not in claimed_cells:
            claimed_cells.add(cell)
            # Add the cell to the set of cells with coal
            coal_cells.add(cell)
            # Increment the minimum number of settlers needed
            min_settlers += 1

    # If both sets are not empty, return the minimum number of settlers needed
    if iron_ore_cells and coal_cells:
        return min_settlers
    else:
        # If one of the sets is empty, return "impossible"
        return "impossible"

def main():
    n, m, k = map(int, input().split())
    o = set(map(int, input().split()))
    c = set(map(int, input().split()))
    graph = [set(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, k, o, c, graph))

if __name__ == "__main__":
    main()

