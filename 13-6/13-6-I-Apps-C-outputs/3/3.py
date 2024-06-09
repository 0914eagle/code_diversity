
def get_input():
    n = int(input())
    numbers = list(map(int, input().split()))
    return n, numbers

def get_possible_moves(n, numbers):
    # Initialize a set to store the possible moves
    possible_moves = set()
    
    # Iterate through the numbers and find the adjacent numbers
    for i in range(n):
        # If the current number is odd, add it to the possible moves
        if numbers[i] % 2 == 1:
            possible_moves.add(numbers[i])
        # If the current number is even, add the adjacent odd numbers to the possible moves
        else:
            if i > 0 and numbers[i-1] % 2 == 1:
                possible_moves.add(numbers[i-1])
            if i < n-1 and numbers[i+1] % 2 == 1:
                possible_moves.add(numbers[i+1])
    
    return possible_moves

def get_winnable_moves(n, numbers, possible_moves):
    # Initialize a set to store the winnable moves
    winnable_moves = set()
    
    # Iterate through the possible moves and find the moves that lead to a win
    for move in possible_moves:
        # If the move is odd, add it to the winnable moves
        if move % 2 == 1:
            winnable_moves.add(move)
        # If the move is even, add the adjacent odd numbers to the winnable moves
        else:
            if move > 1 and move-1 in possible_moves:
                winnable_moves.add(move-1)
            if move < n and move+1 in possible_moves:
                winnable_moves.add(move+1)
    
    return winnable_moves

def main():
    n, numbers = get_input()
    possible_moves = get_possible_moves(n, numbers)
    winnable_moves = get_winnable_moves(n, numbers, possible_moves)
    print(len(winnable_moves))

if __name__ == '__main__':
    main()

