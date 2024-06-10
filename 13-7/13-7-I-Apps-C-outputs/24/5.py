
def get_possible_moves(numbers):
    # Initialize a set to store the possible moves
    possible_moves = set()
    
    # Iterate through the numbers
    for i in range(len(numbers)):
        # Get the current number
        current_number = numbers[i]
        
        # Check if the current number is odd
        if current_number % 2 != 0:
            # If the current number is odd, add it to the set of possible moves
            possible_moves.add(current_number)
        
        # Get the previous number
        previous_number = numbers[(i - 1) % len(numbers)]
        
        # Check if the previous number is odd
        if previous_number % 2 != 0:
            # If the previous number is odd, add it to the set of possible moves
            possible_moves.add(previous_number)
    
    # Return the set of possible moves
    return possible_moves

def get_winning_moves(numbers, possible_moves):
    # Initialize a set to store the winning moves
    winning_moves = set()
    
    # Iterate through the possible moves
    for move in possible_moves:
        # Initialize a flag to check if the move is a winning move
        is_winning_move = True
        
        # Iterate through the numbers
        for i in range(len(numbers)):
            # Get the current number
            current_number = numbers[i]
            
            # Check if the current number is adjacent to the move
            if current_number in [move - 1, move + 1]:
                # If the current number is adjacent to the move, set the flag to False
                is_winning_move = False
                break
        
        # Check if the move is a winning move
        if is_winning_move:
            # If the move is a winning move, add it to the set of winning moves
            winning_moves.add(move)
    
    # Return the set of winning moves
    return winning_moves

def get_number_of_possible_moves(numbers):
    # Get the set of possible moves
    possible_moves = get_possible_moves(numbers)
    
    # Get the set of winning moves
    winning_moves = get_winning_moves(numbers, possible_moves)
    
    # Return the number of possible moves that lead to a win
    return len(winning_moves)

if __name__ == '__main__':
    # Get the number of numbers
    n = int(input())
    
    # Get the numbers
    numbers = list(map(int, input().split()))
    
    # Get the number of possible moves that lead to a win
    number_of_possible_moves = get_number_of_possible_moves(numbers)
    
    # Print the number of possible moves that lead to a win
    print(number_of_possible_moves)

