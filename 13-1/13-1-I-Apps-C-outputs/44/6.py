
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
            # Find the next junction based on the current junction and the road information
            next_junction = get_next_junction(current_junction, roads)
            
            # If the next junction is the starting junction, break the loop
            if next_junction == start:
                break
            
            # Update the current junction to the next junction
            current_junction = next_junction
            
            # Update the current energy to spend based on the road information
            current_energy += get_energy(current_junction, roads)
            
            # Update the number of candies bought
            num_candies += get_candies(current_junction, roads)
        
        # If the number of candies bought is equal to the total number of candies, update the minimum energy to spend
        if num_candies == sum(roads[2] for roads in roads):
            min_energy = min(min_energy, current_energy)
    
    # Return the minimum energy to spend
    return min_energy if min_energy < float('inf') else "Poor girl"

def get_next_junction(current_junction, roads):
    # Find the road that connects the current junction to the next junction
    for road in roads:
        if road[0] == current_junction:
            return road[1]
    return current_junction

def get_energy(current_junction, roads):
    # Find the road that connects the current junction to the next junction
    for road in roads:
        if road[0] == current_junction:
            return road[2] ** 2
    return 0

def get_candies(current_junction, roads):
    # Find the road that connects the current junction to the next junction
    for road in roads:
        if road[0] == current_junction:
            return road[2]
    return 0

if __name__ == '__main__':
    N, M, alpha = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(M)]
    print(get_min_energy(N, M, alpha, roads))

