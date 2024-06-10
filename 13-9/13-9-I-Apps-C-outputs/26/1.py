
def paint_cross(n, p):
    # Initialize the number of crosses as 1
    num_crosses = 1
    # Initialize the current room as 1
    current_room = 1
    # Initialize the number of portal moves as 0
    num_moves = 0
    
    # Loop through each room from 1 to n
    for i in range(1, n + 1):
        # If the current room has an odd number of crosses, use the second portal
        if num_crosses % 2 == 1:
            current_room = p[current_room - 1]
        # Otherwise, use the first portal
        else:
            current_room += 1
        # Increment the number of crosses
        num_crosses += 1
        # Increment the number of portal moves
        num_moves += 1
    
    # Return the number of portal moves
    return num_moves % 1000000007

def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(paint_cross(n, p))

if __name__ == '__main__':
    main()

