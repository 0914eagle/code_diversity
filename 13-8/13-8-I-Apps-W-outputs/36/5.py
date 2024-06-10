
def is_in_check(n, a_x, a_y, b_x, b_y, c_x, c_y):
    # Check if the king is in check
    if a_x == b_x and (a_y == b_y - 1 or a_y == b_y + 1):
        return True
    if a_y == b_y and (a_x == b_x - 1 or a_x == b_x + 1):
        return True
    if abs(a_x - b_x) == abs(a_y - b_y):
        return True
    return False

def can_move_king(n, a_x, a_y, b_x, b_y, c_x, c_y):
    # Check if the king can move to the target location
    if b_x == c_x and (b_y == c_y - 1 or b_y == c_y + 1):
        return True
    if b_y == c_y and (b_x == c_x - 1 or b_x == c_x + 1):
        return True
    if abs(b_x - c_x) == abs(b_y - c_y):
        return True
    return False

def solve(n, a_x, a_y, b_x, b_y, c_x, c_y):
    if is_in_check(n, a_x, a_y, b_x, b_y, c_x, c_y):
        return "NO"
    if can_move_king(n, a_x, a_y, b_x, b_y, c_x, c_y):
        return "YES"
    return "NO"

if __name__ == '__main__':
    n = int(input())
    a_x, a_y = map(int, input().split())
    b_x, b_y = map(int, input().split())
    c_x, c_y = map(int, input().split())
    print(solve(n, a_x, a_y, b_x, b_y, c_x, c_y))

