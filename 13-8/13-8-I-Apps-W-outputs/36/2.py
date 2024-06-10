
def is_checkmate(n, a_x, a_y, b_x, b_y, c_x, c_y):
    # Check if the king is in check
    if is_in_check(n, a_x, a_y, b_x, b_y):
        return False
    
    # Check if the target location is in check
    if is_in_check(n, a_x, a_y, c_x, c_y):
        return False
    
    # Check if the king can move to the target location
    if can_move_to_target(n, a_x, a_y, b_x, b_y, c_x, c_y):
        return True
    
    return False

def is_in_check(n, a_x, a_y, b_x, b_y):
    # Check if the king is on the same rank, file, or diagonal as the queen
    if a_x == b_x or a_y == b_y or abs(a_x - b_x) == abs(a_y - b_y):
        return True
    
    return False

def can_move_to_target(n, a_x, a_y, b_x, b_y, c_x, c_y):
    # Check if the king can move to the target location
    for i in range(1, 8):
        for j in range(1, 8):
            if i != j:
                if can_move_to_square(n, a_x, a_y, b_x, b_y, c_x, c_y, i, j):
                    return True
    
    return False

def can_move_to_square(n, a_x, a_y, b_x, b_y, c_x, c_y, i, j):
    # Check if the king can move to a specific square
    if b_x + i <= n and b_y + j <= n:
        if is_in_check(n, a_x, a_y, b_x + i, b_y + j):
            return False
        if is_in_check(n, a_x, a_y, c_x, c_y):
            return False
        return True
    
    return False

if __name__ == '__main__':
    n = int(input())
    a_x = int(input())
    a_y = int(input())
    b_x = int(input())
    b_y = int(input())
    c_x = int(input())
    c_y = int(input())
    
    if is_checkmate(n, a_x, a_y, b_x, b_y, c_x, c_y):
        print("YES")
    else:
        print("NO")

