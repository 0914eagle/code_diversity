
def get_min_time_to_reach(start_floor, start_section, end_floor, end_section, stairs_positions, elevators_positions):
    # Base case: if start and end floors are the same, return the distance between the sections
    if start_floor == end_floor:
        return abs(start_section - end_section)
    
    # Initialize the minimum time to reach the end floor
    min_time = float('inf')
    
    # Iterate over all possible ways to reach the end floor
    for way in get_ways_to_reach(start_floor, end_floor, stairs_positions, elevators_positions):
        # Calculate the time to reach the end floor using this way
        time = get_time_to_reach(start_floor, start_section, way, stairs_positions, elevators_positions)
        # Update the minimum time if necessary
        min_time = min(min_time, time)
    
    return min_time

def get_ways_to_reach(start_floor, end_floor, stairs_positions, elevators_positions):
    # Initialize the list of ways to reach the end floor
    ways = []
    
    # If the start floor is below the end floor, add the elevator as a way to reach the end floor
    if start_floor < end_floor:
        ways.append(('elevator', end_floor))
    
    # If the start floor is above the end floor, add the stairs as a way to reach the end floor
    if start_floor > end_floor:
        ways.append(('stairs', end_floor))
    
    # Add the direct way from the start floor to the end floor if it's possible
    if start_floor != end_floor:
        ways.append(('direct', end_floor))
    
    return ways

def get_time_to_reach(start_floor, start_section, way, stairs_positions, elevators_positions):
    # Initialize the time to reach the end floor
    time = 0
    
    # If the way is to use the stairs, calculate the time to reach the end floor using the stairs
    if way[0] == 'stairs':
        end_floor = way[1]
        time += abs(start_floor - end_floor) * 2
        time += abs(start_section - stairs_positions[0])
    
    # If the way is to use the elevator, calculate the time to reach the end floor using the elevator
    elif way[0] == 'elevator':
        end_floor = way[1]
        time += abs(start_floor - end_floor) * 2
        time += abs(start_section - elevators_positions[0])
    
    # If the way is to use the direct way, calculate the time to reach the end floor directly
    elif way[0] == 'direct':
        end_floor = way[1]
        time += abs(start_section - end_section)
    
    return time

def main():
    n, m, c_l, c_e, v = map(int, input().split())
    stairs_positions = list(map(int, input().split()))
    elevators_positions = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        print(get_min_time_to_reach(x1, y1, x2, y2, stairs_positions, elevators_positions))

if __name__ == '__main__':
    main()

