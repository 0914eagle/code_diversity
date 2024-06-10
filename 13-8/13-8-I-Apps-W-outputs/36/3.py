
def check_win(n, a_x, a_y, b_x, b_y, c_x, c_y):
    # Check if the king is in check
    if b_x == a_x or b_y == a_y or abs(b_x - a_x) == abs(b_y - a_y):
        return "NO"
    
    # Check if the target location is in check
    if c_x == a_x or c_y == a_y or abs(c_x - a_x) == abs(c_y - a_y):
        return "NO"
    
    # Check if the king can reach the target location without being in check
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != b_x and j != b_y and i != c_x and j != c_y:
                continue
            if abs(i - b_x) + abs(j - b_y) == abs(c_x - b_x) + abs(c_y - b_y):
                return "YES"
    return "NO"

def main():
    n = int(input())
    a_x, a_y = map(int, input().split())
    b_x, b_y = map(int, input().split())
    c_x, c_y = map(int, input().split())
    print(check_win(n, a_x, a_y, b_x, b_y, c_x, c_y))

if __name__ == '__main__':
    main()

