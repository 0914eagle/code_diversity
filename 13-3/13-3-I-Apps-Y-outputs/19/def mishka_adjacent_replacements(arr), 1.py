
def mishka_adjacent_replacements(arr):
    # Replace each occurrence of 1 with 2
    arr = [x if x != 1 else 2 for x in arr]
    # Replace each occurrence of 2 with 1
    arr = [x if x != 2 else 1 for x in arr]
    # Replace each occurrence of 3 with 4
    arr = [x if x != 3 else 4 for x in arr]
    # Replace each occurrence of 4 with 3
    arr = [x if x != 4 else 3 for x in arr]
    # Replace each occurrence of 5 with 6
    arr = [x if x != 5 else 6 for x in arr]
    # Replace each occurrence of 6 with 5
    arr = [x if x != 6 else 5 for x in arr]
    # Replace each occurrence of 7 with 8
    arr = [x if x != 7 else 8 for x in arr]
    # Replace each occurrence of 8 with 7
    arr = [x if x != 8 else 7 for x in arr]
    # Replace each occurrence of 9 with 10
    arr = [x if x != 9 else 10 for x in arr]
    # Replace each occurrence of 10 with 9
    arr = [x if x != 10 else 9 for x in arr]
    return arr

