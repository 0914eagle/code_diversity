
def f1(image):
    # Initialize a dictionary to store the number of islands for each cell
    num_islands = {}
    
    # Loop through each cell in the image
    for row in range(len(image)):
        for col in range(len(image[0])):
            # If the current cell is land and not already counted, count the number of islands it is part of
            if image[row][col] == "L" and (row, col) not in num_islands:
                num_islands[(row, col)] = 1
                queue = [(row, col)]
                
                # Breadth-first search to count the number of islands the current cell is part of
                while queue:
                    curr_row, curr_col = queue.pop(0)
                    for r, c in [(curr_row-1, curr_col), (curr_row+1, curr_col), (curr_row, curr_col-1), (curr_row, curr_col+1)]:
                        if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == "L" and (r, c) not in num_islands:
                            num_islands[(r, c)] = num_islands[(row, col)]
                            queue.append((r, c))
    
    # Return the maximum number of islands
    return max(num_islands.values(), default=0)

def f2(image):
    # Initialize a dictionary to store the number of islands for each cell
    num_islands = {}
    
    # Loop through each cell in the image
    for row in range(len(image)):
        for col in range(len(image[0])):
            # If the current cell is land and not already counted, count the number of islands it is part of
            if image[row][col] == "L" and (row, col) not in num_islands:
                num_islands[(row, col)] = 1
                queue = [(row, col)]
                
                # Breadth-first search to count the number of islands the current cell is part of
                while queue:
                    curr_row, curr_col = queue.pop(0)
                    for r, c in [(curr_row-1, curr_col), (curr_row+1, curr_col), (curr_row, curr_col-1), (curr_row, curr_col+1)]:
                        if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == "L" and (r, c) not in num_islands:
                            num_islands[(r, c)] = num_islands[(row, col)]
                            queue.append((r, c))
    
    # Return the minimum number of islands
    return min(num_islands.values(), default=0)

if __name__ == '__main__':
    image = [
        ['C', 'C', 'C', 'C', 'C'],
        ['C', 'C', 'C', 'C', 'C'],
        ['C', 'C', 'C', 'C', 'C'],
        ['C', 'C', 'C', 'C', 'C']
    ]
    print(f2(image))

