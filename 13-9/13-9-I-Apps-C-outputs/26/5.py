
def get_crosses_needed(n, portals):
    # Initialize variables
    crosses_needed = 0
    current_room = 1

    # Loop through each room
    for i in range(n):
        # If the ceiling contains an odd number of crosses, use the second portal
        if crosses_needed % 2 == 1:
            current_room = portals[current_room - 1]
        # Otherwise, use the first portal
        else:
            current_room += 1

        # Increment the number of crosses needed
        crosses_needed += 1

    # Return the number of crosses needed to get to the last room
    return crosses_needed

def main():
    n = int(input())
    portals = list(map(int, input().split()))
    print(get_crosses_needed(n, portals) % 1000000007)

if __name__ == '__main__':
    main()

