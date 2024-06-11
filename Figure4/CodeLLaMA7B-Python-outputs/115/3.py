def max_fill(grid, capacity):
    import math
    
    # 1. Take the first row and count the number of 1s
    # 2. Take the first column and count the number of 1s
    # 3. Take the first diagonal and count the number of 1s
    # 4. Take the second diagonal and count the number of 1s
    # 5. Take the first row and count the number of 1s
    # 6. Take the first column and count the number of 1s
    # 7. Take the first diagonal and count the number of 1s
    # 8. Take the second diagonal and count the number of 1s
    # 9. Subtract the number of 1s from the capacity
    # 10. If the number of 1s is greater than the capacity, return the number of 1s - capacity
    # 11. Else, return 0
    # 12. Repeat steps 1 - 10 for all rows and columns
    # 13. Return the minimum of the number of 1s - capacity

    # 1. Take the first row and count the number of 1s
    row_1 = sum(grid[0])
    # 2. Take the first column and count the number of 1s
    col_1 = sum(grid[0,:])
    # 3. Take the first diagonal and count the number of 1s
    diag_1 = sum(grid[0,0])
    # 4. Take the second diagonal and count the number of 1s
    diag_2 = sum(grid[0,-1])
    # 5. Take the first row and count the number of 1s
    row_2 = sum(grid[-1])
    # 6. Take the first column and count the number of 1s
    col_2 = sum(grid[:,-1])
    # 7. Take the first diagonal and count the number of 1s
    diag_3 = sum(grid[-1,-1])
    # 8. Take the second diagonal and count the number of 1s
    diag_4 = sum(grid[-1,0])
    # 9. Subtract the number of 1s from the