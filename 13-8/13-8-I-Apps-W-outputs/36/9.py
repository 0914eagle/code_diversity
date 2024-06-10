
def can_king_move(king_x, king_y, target_x, target_y, n):
    # Check if the king is in check
    if king_x == target_x and king_y == target_y:
        return False
    
    # Check if the target square is in check
    if target_x == king_x and target_y == king_y:
        return False
    
    # Check if the king can move to the target square
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == king_x and j == king_y:
                continue
            if i == target_x and j == target_y:
                return True
    
    return False

def can_queen_move(queen_x, queen_y, king_x, king_y, target_x, target_y, n):
    # Check if the queen is in check
    if queen_x == king_x and queen_y == king_y:
        return False
    
    # Check if the queen can move to the target square
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == queen_x and j == queen_y:
                continue
            if i == target_x and j == target_y:
                return True
    
    return False

def solve(n, a_x, a_y, b_x, b_y, c_x, c_y):
    # Check if the king is in check
    if b_x == c_x and b_y == c_y:
        return "NO"
    
    # Check if the target square is in check
    if c_x == a_x and c_y == a_y:
        return "NO"
    
    # Check if the king can move to the target square
    if can_king_move(b_x, b_y, c_x, c_y, n):
        return "YES"
    
    # Check if the queen can move to the target square
    if can_queen_move(a_x, a_y, b_x, b_y, c_x, c_y, n):
        return "YES"
    
    return "NO"

if __name__ == '__main__':
    n = int(input())
    a_x, a_y = map(int, input().split())
    b_x, b_y = map(int, input().split())
    c_x, c_y = map(int, input().split())
    print(solve(n, a_x, a_y, b_x, b_y, c_x, c_y))

