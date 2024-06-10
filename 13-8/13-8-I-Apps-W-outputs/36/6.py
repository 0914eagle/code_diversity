
def is_check(king_x, king_y, queen_x, queen_y):
    # Check if the king is in check
    if king_x == queen_x and (king_y == queen_y + 1 or king_y == queen_y - 1):
        return True
    elif king_y == queen_y and (king_x == queen_x + 1 or king_x == queen_x - 1):
        return True
    elif abs(king_x - queen_x) == abs(king_y - queen_y):
        return True
    else:
        return False

def solve(n, a_x, a_y, b_x, b_y, c_x, c_y):
    # Check if the king is in check
    if is_check(b_x, b_y, a_x, a_y):
        return "NO"
    
    # Check if the target location is in check
    if is_check(c_x, c_y, a_x, a_y):
        return "NO"
    
    # Check if the king can move to the target location
    if abs(b_x - c_x) <= 1 and abs(b_y - c_y) <= 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    n = int(input())
    a_x, a_y = map(int, input().split())
    b_x, b_y = map(int, input().split())
    c_x, c_y = map(int, input().split())
    print(solve(n, a_x, a_y, b_x, b_y, c_x, c_y))

