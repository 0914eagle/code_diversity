
def get_min_max_occupied_houses(n, x):
    # Initialize the minimum and maximum number of occupied houses
    min_occupied_houses = 0
    max_occupied_houses = 0
    
    # Loop through each friend and their possible moves
    for i in range(n):
        # Get the current and possible moves for the friend
        current_move = x[i]
        possible_moves = [current_move - 1, current_move + 1]
        
        # Check if the friend can move to a house with a coordinate of 0 or n + 1
        if current_move == 1:
            possible_moves.append(0)
        elif current_move == n:
            possible_moves.append(n + 1)
        
        # Loop through each possible move and check if it is already occupied
        for move in possible_moves:
            if move not in x:
                # If the move is not already occupied, increment the maximum number of occupied houses
                max_occupied_houses += 1
            else:
                # If the move is already occupied, increment the minimum number of occupied houses
                min_occupied_houses += 1
    
    return min_occupied_houses, max_occupied_houses

def main():
    n = int(input())
    x = list(map(int, input().split()))
    min_occupied_houses, max_occupied_houses = get_min_max_occupied_houses(n, x)
    print(min_occupied_houses, max_occupied_houses)

if __name__ == '__main__':
    main()

