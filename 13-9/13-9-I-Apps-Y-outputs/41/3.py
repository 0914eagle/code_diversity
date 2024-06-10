
def count_white_cells(H, W, h, w):
    # Calculate the number of cells in the selected rows and columns
    num_cells = h * W + W * w - h * w
    # Return the number of white cells that will remain
    return H * W - num_cells

def main():
    # Read the input data from stdin
    H, W, h, w = map(int, input().split())
    # Calculate the number of white cells that will remain
    num_white_cells = count_white_cells(H, W, h, w)
    # Print the result
    print(num_white_cells)

if __name__ == '__main__':
    main()

