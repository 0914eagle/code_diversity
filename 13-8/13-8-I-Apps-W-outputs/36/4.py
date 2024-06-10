
def get_king_moves(king_pos, n):
    
    king_moves = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if abs(king_pos[0] - i) + abs(king_pos[1] - j) == 1:
                king_moves.append((i, j))
    return king_moves

def is_king_safe(king_pos, queen_pos, n):
    
    king_moves = get_king_moves(king_pos, n)
    for move in king_moves:
        if move == queen_pos:
            return False
    return True

def can_king_reach_target(king_pos, queen_pos, target_pos, n):
    
    king_moves = get_king_moves(king_pos, n)
    for move in king_moves:
        if move == target_pos:
            return True
        if is_king_safe(move, queen_pos, n):
            if can_king_reach_target(move, queen_pos, target_pos, n):
                return True
    return False

def main():
    n = int(input())
    a_x, a_y = map(int, input().split())
    b_x, b_y = map(int, input().split())
    c_x, c_y = map(int, input().split())
    if can_king_reach_target((b_x, b_y), (a_x, a_y), (c_x, c_y), n):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

