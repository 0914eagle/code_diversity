
def f1(player, n, cuboids):
    # Initialize the game state
    state = {}
    for i in range(n):
        state[i] = cuboids[i]
    
    # Play the game
    while len(state) > 0:
        # Choose a cuboid to cut
        cuboid_id = choose_cuboid(state)
        cuboid = state[cuboid_id]
        
        # Cut the cuboid
        new_cuboids = cut_cuboid(cuboid)
        
        # Remove the cuboid from the state
        del state[cuboid_id]
        
        # Add the new cuboids to the state
        for i, new_cuboid in enumerate(new_cuboids):
            state[cuboid_id * 10 + i] = new_cuboid
    
    # Determine the winner
    if player == "RUBEN":
        return "RUBEN"
    else:
        return "ALBERT"

def f2(player, n, cuboids):
    # Initialize the game state
    state = {}
    for i in range(n):
        state[i] = cuboids[i]
    
    # Play the game
    while len(state) > 0:
        # Choose a cuboid to cut
        cuboid_id = choose_cuboid(state)
        cuboid = state[cuboid_id]
        
        # Cut the cuboid
        new_cuboids = cut_cuboid(cuboid)
        
        # Remove the cuboid from the state
        del state[cuboid_id]
        
        # Add the new cuboids to the state
        for i, new_cuboid in enumerate(new_cuboids):
            state[cuboid_id * 10 + i] = new_cuboid
    
    # Determine the winner
    if player == "RUBEN":
        return "RUBEN"
    else:
        return "ALBERT"

def choose_cuboid(state):
    # Choose a cuboid to cut
    return max(state, key=lambda x: state[x][0] * state[x][1] * state[x][2])

def cut_cuboid(cuboid):
    # Cut the cuboid
    x, y, z = cuboid
    new_cuboids = []
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            for k in range(1, z + 1):
                if i != x or j != y or k != z:
                    new_cuboids.append((i, j, k))
    return new_cuboids

if __name__ == '__main__':
    player = input()
    n = int(input())
    cuboids = []
    for i in range(n):
        x, y, z = map(int, input().split())
        cuboids.append((x, y, z))
    print(f1(player, n, cuboids))
    print(f2(player, n, cuboids))

