
def get_shortcuts(k):
    # Define shortcuts for the given value of k
    shortcuts = {}
    shortcuts["R"] = "SrS"
    shortcuts["S"] = "rr"
    shortcuts["I"] = "lldll"
    return shortcuts

def get_moves(k, organs, empty_space):
    # Initialize variables
    moves = []
    organs_to_move = []
    empty_space_index = organs.index(empty_space)

    # Identify the organs that need to be moved
    for i in range(len(organs)):
        if organs[i] != empty_space and organs[i] != organs[empty_space_index]:
            organs_to_move.append(organs[i])

    # Generate the moves
    for i in range(len(organs_to_move)):
        # Move the organ to the left of the empty space
        if empty_space_index > 0 and organs_to_move[i] == organs[empty_space_index - 1]:
            moves.append("l")
        # Move the organ to the right of the empty space
        elif empty_space_index < len(organs) - 1 and organs_to_move[i] == organs[empty_space_index + 1]:
            moves.append("r")
        # Move the organ up
        elif empty_space_index >= k + 1 and organs_to_move[i] == organs[empty_space_index - k - 1]:
            moves.append("u")
        # Move the organ down
        elif empty_space_index < len(organs) - k - 1 and organs_to_move[i] == organs[empty_space_index + k + 1]:
            moves.append("d")
        # If the move is not possible, return False
        else:
            return False

    return moves

def get_solution(k, organs, empty_space):
    # Get the shortcuts for the given value of k
    shortcuts = get_shortcuts(k)

    # Generate the moves
    moves = get_moves(k, organs, empty_space)

    # If the moves are not possible, return False
    if not moves:
        return False

    # Expand the moves using the shortcuts
    solution = []
    for move in moves:
        if move in shortcuts:
            solution.append(shortcuts[move])
        else:
            solution.append(move)

    return "".join(solution)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        k = int(input())
        organs = list(map(int, input().split()))
        empty_space = int(input())
        solution = get_solution(k, organs, empty_space)
        if solution:
            print("SURGERY COMPLETE")
            print(solution)
            print("DONE")
        else:
            print("SURGERY FAILED")

