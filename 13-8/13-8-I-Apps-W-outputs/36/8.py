
def is_check(n, a_x, a_y, b_x, b_y, c_x, c_y):
    # Check if the king is in check
    if a_x == b_x and a_y == b_y:
        return True
    
    # Check if the king is on the same rank as the queen
    if a_x == c_x:
        return True
    
    # Check if the king is on the same file as the queen
    if a_y == c_y:
        return True
    
    # Check if the king is on the same diagonal as the queen
    if abs(a_x - c_x) == abs(a_y - c_y):
        return True
    
    return False

def can_win(n, a_x, a_y, b_x, b_y, c_x, c_y):
    # Base case: If the king is already in the target location, return True
    if b_x == c_x and b_y == c_y:
        return True
    
    # Check if the king is in check
    if is_check(n, a_x, a_y, b_x, b_y, c_x, c_y):
        return False
    
    # Recursive case: Try all possible moves for the king and check if any of them lead to a win
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != b_x and j != b_y:
                if can_win(n, a_x, a_y, i, j, c_x, c_y):
                    return True
    
    return False

def main():
    n = int(input())
    a_x, a_y = map(int, input().split())
    b_x, b_y = map(int, input().split())
    c_x, c_y = map(int, input().split())
    
    if can_win(n, a_x, a_y, b_x, b_y, c_x, c_y):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

