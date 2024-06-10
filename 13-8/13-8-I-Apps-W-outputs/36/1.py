
def is_king_in_check(king_x, king_y, queen_x, queen_y, n):
    # Check if the king is in the same rank as the queen
    if king_x == queen_x:
        return True
    
    # Check if the king is in the same file as the queen
    if king_y == queen_y:
        return True
    
    # Check if the king is in any of the 8 adjacent squares
    for i in range(1, n+1):
        if (king_x == queen_x+i and king_y == queen_y+i) or (king_x == queen_x-i and king_y == queen_y-i) or (king_x == queen_x+i and king_y == queen_y-i) or (king_x == queen_x-i and king_y == queen_y+i) or (king_x == queen_x+i and king_y == queen_y) or (king_x == queen_x-i and king_y == queen_y) or (king_x == queen_x and king_y == queen_y+i) or (king_x == queen_x and king_y == queen_y-i):
            return True
    
    return False

def can_king_move(king_x, king_y, queen_x, queen_y, n):
    # Check if the king is in check
    if is_king_in_check(king_x, king_y, queen_x, queen_y, n):
        return False
    
    # Check if the king can move to any of the 8 adjacent squares
    for i in range(1, n+1):
        if (king_x+i, king_y+i) not in [(queen_x+i, queen_y+i) for i in range(1, n+1)] and (king_x+i, king_y-i) not in [(queen_x+i, queen_y-i) for i in range(1, n+1)] and (king_x-i, king_y+i) not in [(queen_x-i, queen_y+i) for i in range(1, n+1)] and (king_x-i, king_y-i) not in [(queen_x-i, queen_y-i) for i in range(1, n+1)] and (king_x+i, king_y) not in [(queen_x+i, queen_y) for i in range(1, n+1)] and (king_x-i, king_y) not in [(queen_x-i, queen_y) for i in range(1, n+1)] and (king_x, king_y+i) not in [(queen_x, queen_y+i) for i in range(1, n+1)] and (king_x, king_y-i) not in [(queen_x, queen_y-i) for i in range(1, n+1)]:
            return True
    
    return False

def main():
    n = int(input())
    a_x, a_y = map(int, input().split())
    b_x, b_y = map(int, input().split())
    c_x, c_y = map(int, input().split())
    
    if can_king_move(b_x, b_y, a_x, a_y, n):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

