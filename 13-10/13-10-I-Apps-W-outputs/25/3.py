
def get_min_time(n_floors, n_sections, stairs, elevators, max_speed, queries):
    # Initialize a dictionary to store the minimum time needed to go from one section to another
    min_time = {}
    
    # Loop through each floor and section
    for i in range(n_floors):
        for j in range(n_sections):
            # Initialize the minimum time to go from this section to any other section as infinity
            min_time[(i, j)] = float('inf')
    
    # Loop through each stair
    for stair in stairs:
        # Get the position of the stair
        stair_pos = stair[0]
        # Loop through each floor
        for i in range(n_floors):
            # Loop through each section on this floor
            for j in range(n_sections):
                # If the stair is located in this section, set the minimum time to go from this section to any other section on the same floor as 1
                if j == stair_pos:
                    min_time[(i, j)] = 1
    
    # Loop through each elevator
    for elevator in elevators:
        # Get the position of the elevator
        elevator_pos = elevator[0]
        # Loop through each floor
        for i in range(n_floors):
            # Loop through each section on this floor
            for j in range(n_sections):
                # If the elevator is located in this section, set the minimum time to go from this section to any other section on the same floor as the maximum speed of the elevator
                if j == elevator_pos:
                    min_time[(i, j)] = max_speed
    
    # Loop through each query
    for query in queries:
        # Get the starting and ending sections for the query
        start_section = (query[0], query[1])
        end_section = (query[2], query[3])
        # Initialize the minimum time needed for the query as infinity
        min_time_needed = float('inf')
        # Loop through each section on the path from the starting section to the ending section
        for section in range(start_section[1], end_section[1] + 1):
            # If the minimum time needed to go from the starting section to this section is less than the current minimum time needed, update the minimum time needed
            if min_time[(start_section[0], section)] < min_time_needed:
                min_time_needed = min_time[(start_section[0], section)]
        # Loop through each section on the path from the ending section to the starting section
        for section in range(end_section[1], start_section[1] - 1, -1):
            # If the minimum time needed to go from the ending section to this section is less than the current minimum time needed, update the minimum time needed
            if min_time[(end_section[0], section)] < min_time_needed:
                min_time_needed = min_time[(end_section[0], section)]
        # Add the minimum time needed to go from the starting section to the ending section
        min_time_needed += min_time[(start_section[0], start_section[1])]
    
    return min_time_needed

def main():
    n_floors, n_sections, c_l, c_e, max_speed = map(int, input().split())
    stairs = []
    elevators = []
    for _ in range(c_l):
        stairs.append(int(input()))
    for _ in range(c_e):
        elevators.append(int(input()))
    queries = []
    for _ in range(int(input())):
        queries.append(list(map(int, input().split())))
    
    print(get_min_time(n_floors, n_sections, stairs, elevators, max_speed, queries))

if __name__ == '__main__':
    main()

