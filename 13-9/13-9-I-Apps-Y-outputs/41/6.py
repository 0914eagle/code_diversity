
def get_input():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    return H, W, h, w

def paint_cells(H, W, h, w):
    # Initialize a 2D array of cells with all cells set to white
    cells = [[1] * W for _ in range(H)]
    
    # Paint the chosen rows and columns black
    for i in range(h):
        for j in range(W):
            cells[i][j] = 0
    for i in range(H):
        for j in range(w):
            cells[i][j] = 0
    
    # Count the number of white cells that remain
    count = 0
    for i in range(H):
        for j in range(W):
            if cells[i][j] == 1:
                count += 1
    
    return count

def main():
    H, W, h, w = get_input()
    print(paint_cells(H, W, h, w))

if __name__ == '__main__':
    main()

