
def get_min_cost(costs, next_rooms):
    # Initialize the minimum cost and the set of rooms with traps
    min_cost = 0
    rooms_with_traps = set()

    # Loop through the costs and next rooms
    for i, (cost, next_room) in enumerate(zip(costs, next_rooms)):
        # If the current room is not in the set of rooms with traps, add it and update the minimum cost
        if i not in rooms_with_traps:
            min_cost += cost
            rooms_with_traps.add(i)

        # If the next room is in the set of rooms with traps, add it and update the minimum cost
        if next_room in rooms_with_traps:
            min_cost += cost
            rooms_with_traps.add(next_room)

    return min_cost

def main():
    # Read the number of rooms and the costs and next rooms from stdin
    n = int(input())
    costs = list(map(int, input().split()))
    next_rooms = list(map(int, input().split()))

    # Call the get_min_cost function and print the result
    print(get_min_cost(costs, next_rooms))

if __name__ == '__main__':
    main()

