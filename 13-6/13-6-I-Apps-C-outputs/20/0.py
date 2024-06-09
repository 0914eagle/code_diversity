
def f1(arr):
    # Check if the input array is a valid cube
    if len(arr) != 6 or len(arr[0]) != 6:
        return "cannot fold"
    
    # Check if the input array is a connected component
    if not is_connected(arr):
        return "cannot fold"
    
    # Check if the input array contains a 2x2 subsquare
    if has_2x2_subsquare(arr):
        return "cannot fold"
    
    # Check if the input array can be folded into a cube
    if can_fold(arr):
        return "can fold"
    else:
        return "cannot fold"

def f2(arr):
    # Check if the input array is a valid cube
    if len(arr) != 6 or len(arr[0]) != 6:
        return "cannot fold"
    
    # Check if the input array is a connected component
    if not is_connected(arr):
        return "cannot fold"
    
    # Check if the input array contains a 2x2 subsquare
    if has_2x2_subsquare(arr):
        return "cannot fold"
    
    # Check if the input array can be folded into a cube
    if can_fold(arr):
        return "can fold"
    else:
        return "cannot fold"

def is_connected(arr):
    # Check if the input array is a connected component
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "#":
                if not can_reach(arr, i, j):
                    return False
    return True

def can_reach(arr, i, j):
    # Check if the current square can be reached from any other square
    for k in range(len(arr)):
        for l in range(len(arr[0])):
            if arr[k][l] == "#" and (k != i or l != j):
                if can_reach(arr, k, l):
                    return True
    return False

def has_2x2_subsquare(arr):
    # Check if the input array contains a 2x2 subsquare
    for i in range(len(arr) - 1):
        for j in range(len(arr[0]) - 1):
            if arr[i][j] == "#" and arr[i][j + 1] == "#" and arr[i + 1][j] == "#" and arr[i + 1][j + 1] == "#":
                return True
    return False

def can_fold(arr):
    # Check if the input array can be folded into a cube
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "#":
                if not can_fold_square(arr, i, j):
                    return False
    return True

def can_fold_square(arr, i, j):
    # Check if the current square can be folded into a cube
    for k in range(len(arr)):
        for l in range(len(arr[0])):
            if arr[k][l] == "#" and (k != i or l != j):
                if can_fold_square(arr, k, l):
                    return True
    return False

if __name__ == '__main__':
    arr = [
        [".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "."],
        ["#", "#", "#", "#", "#", "#"],
        [".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "."]
    ]
    print(f1(arr))
    print(f2(arr))

