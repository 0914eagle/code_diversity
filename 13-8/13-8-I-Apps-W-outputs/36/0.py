
def is_check(n, a_x, a_y, b_x, b_y, c_x, c_y):
    # Check if the king is in check
    if a_x == b_x and (a_y == b_y + 1 or a_y == b_y - 1):
        return True
    if a_y == b_y and (a_x == b_x + 1 or a_x == b_x - 1):
        return True
    if abs(a_x - b_x) == abs(a_y - b_y):
        return True
    return False

def is_move_possible(n, a_x, a_y, b_x, b_y, c_x, c_y):
    # Check if the move is possible
    if c_x < 1 or c_x > n or c_y < 1 or c_y > n:
        return False
    if abs(c_x - b_x) > 1 or abs(c_y - b_y) > 1:
        return False
    return True

def can_king_move_to_c(n, a_x, a_y, b_x, b_y, c_x, c_y):
    # Check if the king can move to the target location without getting in check
    if not is_move_possible(n, a_x, a_y, b_x, b_y, c_x, c_y):
        return False
    if is_check(n, a_x, a_y, b_x, b_y, c_x, c_y):
        return False
    return True

def main():
    n = int(input())
    a_x, a_y = map(int, input().split())
    b_x, b_y = map(int, input().split())
    c_x, c_y = map(int, input().split())
    if can_king_move_to_c(n, a_x, a_y, b_x, b_y, c_x, c_y):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

