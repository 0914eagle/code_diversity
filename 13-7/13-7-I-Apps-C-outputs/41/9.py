
def get_shortcuts(k):
    # Function to get the shortcuts for the test case
    shortcuts = {}
    for i in range(1, k+1):
        shortcuts[chr(i+64)] = "l" * i
    shortcuts["R"] = "SrS"
    shortcuts["S"] = "rr"
    shortcuts["I"] = "lldll"
    return shortcuts

def get_moves(k, organs, empty_space):
    # Function to get the moves for the test case
    moves = []
    for i in range(1, k+1):
        if organs[i] != i:
            moves.append("l")
        if organs[i+k] != i+k:
            moves.append("d")
    if empty_space != k+1:
        moves.append("I")
    return moves

def get_sequence(k, organs, empty_space):
    # Function to get the sequence of moves for the test case
    shortcuts = get_shortcuts(k)
    moves = get_moves(k, organs, empty_space)
    sequence = ""
    for move in moves:
        if move in shortcuts:
            sequence += move
        else:
            sequence += shortcuts[move]
    return sequence

def main():
    # Main function for the program
    test_cases = int(input())
    for _ in range(test_cases):
        k = int(input())
        organs = [int(i) for i in input().split()]
        empty_space = int(input())
        if empty_space != k+1:
            print("SURGERY COMPLETE")
            print(get_sequence(k, organs, empty_space))
        else:
            print("SURGERY FAILED")

if __name__ == '__main__':
    main()

