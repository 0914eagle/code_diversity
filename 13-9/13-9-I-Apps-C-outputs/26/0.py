
def get_number_of_portals(n, portals):
    # Initialize the number of portals as 0
    number_of_portals = 0
    
    # Initialize the current room as 1
    current_room = 1
    
    # Iterate through the portals
    for portal in portals:
        # If the ceiling contains an odd number of crosses, use the second portal
        if current_room % 2 == 1:
            current_room = portal
        # Otherwise, use the first portal
        else:
            current_room += 1
        
        # Increment the number of portals
        number_of_portals += 1
    
    # Return the number of portals modulo 1000000007
    return number_of_portals % 1000000007

def main():
    n = int(input())
    portals = list(map(int, input().split()))
    print(get_number_of_portals(n, portals))

if __name__ == '__main__':
    main()

