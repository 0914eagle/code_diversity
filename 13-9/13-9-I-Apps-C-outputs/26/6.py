
def get_portals(n, portals):
    # Initialize a list to store the number of portals needed for each room
    portals_needed = [0] * (n + 1)
    
    # Set the initial room to 1 and the initial number of portals needed to 0
    current_room = 1
    portals_needed[current_room] = 0
    
    # Loop through each room
    for i in range(1, n + 1):
        # If the current room has an odd number of portals needed, use the second portal
        if portals_needed[current_room] % 2 == 1:
            current_room = portals[current_room - 1]
        # Otherwise, use the first portal
        else:
            current_room += 1
        
        # Increment the number of portals needed for the current room
        portals_needed[current_room] += 1
    
    # Return the number of portals needed to get to the last room
    return portals_needed[-1]

def main():
    n = int(input())
    portals = [int(x) for x in input().split()]
    print(get_portals(n, portals) % 1000000007)

if __name__ == '__main__':
    main()

