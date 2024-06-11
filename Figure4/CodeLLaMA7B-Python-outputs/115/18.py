def max_fill(grid, capacity):
    import math
    
    # --------------------------------------------------------------------------
    # The idea is to use a greedy approach.
    # We will start with the first row and try to fill the buckets with water
    # from the first column.
    # If the bucket is full, we will move to the next column.
    # If the bucket is not full, we will try to fill it with water from the next
    # column.
    # If we reach the last column and the bucket is not full, we will move to the
    # next row and try to fill the bucket with water from the first column.
    # If we reach the last row and the bucket is not full, we will move to the
    # next row and try to fill the bucket with water from the first column.
    # If we reach the last row and the bucket is still not full, we will return
    # the number of times we moved the buckets.
    # --------------------------------------------------------------------------
    import math

    