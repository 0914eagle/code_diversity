
def is_king_in_check(king_x, king_y, queen_x, queen_y, n):
    # Check if the king is in the same rank as the queen
    if king_x == queen_x:
        return True
    
    # Check if the king is in the same file as the queen
    if king_y == queen_y:
        return True
    
    # Check if the king is in the same diagonal as the queen
    if abs(king_x - queen_x) == abs(king_y - queen_y):
        return True
    
    return False

def can_king_move_to_target(king_x, king_y, target_x, target_y, n):
    # Check if the target square is not in check
    if is_king_in_check(target_x, target_y, king_x, king_y, n):
        return False
    
    # Check if the king can move to the target square
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and i != target_x and j != target_y:
                if abs(i - target_x) == abs(j - target_y):
                    return True
    
    return False

def main():
    n = int(input())
    a_x, a_y = map(int, input().split())
    b_x, b_y = map(int, input().split())
    c_x, c_y = map(int, input().split())
    
    if is_king_in_check(b_x, b_y, a_x, a_y, n):
        print("NO")
    elif can_king_move_to_target(b_x, b_y, c_x, c_y, n):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

