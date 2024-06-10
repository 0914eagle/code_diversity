
def get_possible_moves(numbers):
    # Initialize a set to store the possible moves
    possible_moves = set()
    
    # Iterate over the numbers and find the adjacent numbers
    for i in range(len(numbers)):
        # Find the adjacent numbers
        adjacent_numbers = [numbers[i-1], numbers[i+1]]
        # If the current number is the first or last number, find the adjacent number wrapping around the circle
        if i == 0:
            adjacent_numbers.append(numbers[-1])
        elif i == len(numbers) - 1:
            adjacent_numbers.append(numbers[0])
        # Add the adjacent numbers to the set of possible moves
        possible_moves.update(adjacent_numbers)
    
    # Return the set of possible moves
    return possible_moves

def get_winnable_moves(numbers, possible_moves):
    # Initialize a set to store the winnable moves
    winnable_moves = set()
    
    # Iterate over the possible moves and find the moves that lead to a win
    for move in possible_moves:
        # Find the number of odd numbers in the sequence of moves leading up to the current move
        num_odd_numbers = 0
        for i in range(len(numbers)):
            if numbers[i] == move:
                break
            if numbers[i] % 2 == 1:
                num_odd_numbers += 1
        # If the number of odd numbers is odd, the move is winnable
        if num_odd_numbers % 2 == 1:
            winnable_moves.add(move)
    
    # Return the set of winnable moves
    return winnable_moves

def main():
    # Read the input
    N = int(input())
    numbers = list(map(int, input().split()))
    
    # Get the possible moves
    possible_moves = get_possible_moves(numbers)
    
    # Get the winnable moves
    winnable_moves = get_winnable_moves(numbers, possible_moves)
    
    # Print the number of winnable moves
    print(len(winnable_moves))

if __name__ == '__main__':
    main()

