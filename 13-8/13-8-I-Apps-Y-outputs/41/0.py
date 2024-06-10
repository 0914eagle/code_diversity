
def paint_square(s, i, j, H, W):
    # Base case: if the square is already black, return True
    if s[i][j] == '#':
        return True
    
    # If the square is white, try painting it black
    s[i][j] = '#'
    
    # Check if the objective is achieved
    if is_objective_achieved(s, H, W):
        return True
    
    # If not, revert the change and try painting the adjacent squares
    s[i][j] = '.'
    for row in range(max(i-1, 0), min(i+2, H)):
        for col in range(max(j-1, 0), min(j+2, W)):
            if row != i or col != j:
                if paint_square(s, row, col, H, W):
                    return True
    
    # If all adjacent squares are tried and failed, return False
    return False

def is_objective_achieved(s, H, W):
    # Check if all squares with value '#' are black
    for i in range(H):
        for j in range(W):
            if s[i][j] == '#' and s[i][j] != '#':
                return False
    
    # Check if all squares with value '.' are white
    for i in range(H):
        for j in range(W):
            if s[i][j] == '.' and s[i][j] != '.':
                return False
    
    # If all squares are as required, return True
    return True

def main():
    H, W = map(int, input().split())
    s = [input() for _ in range(H)]
    if paint_square(s, 0, 0, H, W):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

