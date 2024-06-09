
def f1(a, b, c, d, x, y, x1, y1, x2, y2):
    # check if the starting point is within the allowed range
    if not (x1 <= x <= x2 and y1 <= y <= y2):
        return "NO"
    
    # check if the total number of moves is valid
    if a + b + c + d == 0:
        return "NO"
    
    # perform the moves
    moves = []
    for i in range(a):
        moves.append(("left", x - 1, y))
    for i in range(b):
        moves.append(("right", x + 1, y))
    for i in range(c):
        moves.append(("down", x, y - 1))
    for i in range(d):
        moves.append(("up", x, y + 1))
    
    # check if the moves are valid
    for move in moves:
        if not (x1 <= move[1] <= x2 and y1 <= move[2] <= y2):
            return "NO"
    
    return "YES"

def f2(t):
    for i in range(t):
        a, b, c, d = map(int, input().split())
        x, y, x1, y1, x2, y2 = map(int, input().split())
        print(f1(a, b, c, d, x, y, x1, y1, x2, y2))

if __name__ == '__main__':
    t = int(input())
    f2(t)

