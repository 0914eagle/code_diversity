
def get_min_cost(c_list, a_list):
    # Initialize variables
    n = len(c_list)
    cost = 0
    visited = set()
    current_room = 0
    
    # Loop through the list of rooms
    for i in range(n):
        # If the current room is not visited, visit it and add the cost to the total cost
        if current_room not in visited:
            cost += c_list[current_room]
            visited.add(current_room)
        # Move the mouse to the next room
        current_room = a_list[current_room]
    
    # Return the total cost
    return cost

def solve(n, c_list, a_list):
    # Initialize variables
    min_cost = float('inf')
    visited = set()
    
    # Loop through the list of rooms
    for i in range(n):
        # If the current room is not visited, visit it and calculate the cost
        if i not in visited:
            visited.add(i)
            cost = get_min_cost(c_list, a_list)
            min_cost = min(min_cost, cost)
    
    # Return the minimum cost
    return min_cost

if __name__ == '__main__':
    n = int(input())
    c_list = list(map(int, input().split()))
    a_list = list(map(int, input().split()))
    print(solve(n, c_list, a_list))

