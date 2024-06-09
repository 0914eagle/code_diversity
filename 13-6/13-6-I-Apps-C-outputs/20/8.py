
def f1(arr):
    # Check if the input array is a valid cube
    if len(arr) != 6 or len(arr[0]) != 6:
        return "cannot fold"
    
    # Check if the input array is a connected component
    if not is_connected(arr):
        return "cannot fold"
    
    # Check if the input array has a 2x2 square
    if has_2x2_square(arr):
        return "cannot fold"
    
    # If all checks pass, return "can fold"
    return "can fold"

def f2(arr):
    # Check if the input array is a valid cube
    if len(arr) != 6 or len(arr[0]) != 6:
        return "cannot fold"
    
    # Check if the input array is a connected component
    if not is_connected(arr):
        return "cannot fold"
    
    # Check if the input array has a 2x2 square
    if has_2x2_square(arr):
        return "cannot fold"
    
    # If all checks pass, return "can fold"
    return "can fold"

def is_connected(arr):
    # Check if the input array is a connected component
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "#" and (i == 0 or j == 0 or i == len(arr) - 1 or j == len(arr[0]) - 1):
                return False
    return True

def has_2x2_square(arr):
    # Check if the input array has a 2x2 square
    for i in range(len(arr) - 1):
        for j in range(len(arr[0]) - 1):
            if arr[i][j] == "#" and arr[i + 1][j] == "#" and arr[i][j + 1] == "#" and arr[i + 1][j + 1] == "#":
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

