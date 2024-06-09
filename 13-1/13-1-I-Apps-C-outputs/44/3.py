
def get_min_energy(N, M, alpha, roads):
    # Initialize the minimum energy to spend as infinity
    min_energy = float('inf')
    
    # Loop through all possible starting junctions
    for start in range(1, N + 1):
        # Initialize the current energy to spend as 0
        current_energy = 0
        
        # Initialize the current junction as the starting junction
        current_junction = start
        
        # Initialize the number of candies bought as 0
        num_candies = 0
        
        # Loop through all possible roads
        for _ in range(M):
            # Find the road that connects the current junction to the next junction
            next_junction = get_next_junction(current_junction, roads)
            
            # If there is no next junction, break the loop
            if next_junction == -1:
                break
            
            # Get the number of candies on the current road
            num_candies += get_num_candies(current_junction, next_junction, roads)
            
            # Update the current energy to spend
            current_energy += alpha * num_candies
            
            # Update the current junction
            current_junction = next_junction
        
        # If the current energy to spend is less than the minimum energy, update the minimum energy
        if current_energy < min_energy:
            min_energy = current_energy
    
    # Return the minimum energy to spend
    return min_energy

def get_next_junction(current_junction, roads):
    # Loop through all roads
    for road in roads:
        # If the current junction is the starting junction of the road, return the ending junction
        if road[0] == current_junction:
            return road[1]
    
    # If there is no next junction, return -1
    return -1

def get_num_candies(current_junction, next_junction, roads):
    # Loop through all roads
    for road in roads:
        # If the current junction and next junction are the starting and ending junctions of the road, return the number of candies
        if road[0] == current_junction and road[1] == next_junction:
            return road[2]
    
    # If there is no number of candies, return 0
    return 0

if __name__ == '__main__':
    N, M, alpha = map(int, input().split())
    roads = []
    for _ in range(M):
        u, v, c = map(int, input().split())
        roads.append([u, v, c])
    print(get_min_energy(N, M, alpha, roads))

