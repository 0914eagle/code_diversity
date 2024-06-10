
def get_input():
    N = int(input())
    numbers = list(map(int, input().split()))
    return N, numbers

def get_first_moves(N, numbers):
    first_moves = []
    for i in range(N):
        for j in range(N):
            if i != j and numbers[i] != numbers[j]:
                first_moves.append((i, j))
    return first_moves

def get_winning_moves(first_move, numbers):
    winning_moves = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            winning_moves.append(i)
    return winning_moves

def get_winning_first_moves(first_moves, numbers):
    winning_first_moves = []
    for first_move in first_moves:
        if first_move in get_winning_moves(first_move, numbers):
            winning_first_moves.append(first_move)
    return winning_first_moves

def main():
    N, numbers = get_input()
    first_moves = get_first_moves(N, numbers)
    winning_first_moves = get_winning_first_moves(first_moves, numbers)
    print(len(winning_first_moves))

if __name__ == '__main__':
    main()

