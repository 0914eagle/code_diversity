
def get_white_cells(H, W, h, w):
    # Calculate the total number of cells
    total_cells = H * W
    # Calculate the number of cells in the chosen rows and columns
    chosen_cells = h * W + H * w
    # Calculate the number of white cells that will remain
    white_cells = total_cells - chosen_cells
    return white_cells

def main():
    # Read the input
    H, W, h, w = map(int, input().split())
    # Calculate the number of white cells that will remain
    white_cells = get_white_cells(H, W, h, w)
    # Print the result
    print(white_cells)

if __name__ == '__main__':
    main()

